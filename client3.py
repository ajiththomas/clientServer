import socket
import ssl

#openssl req -new -x509 -keyout server.key -out server.crt -days 365 -nodes

# Server details (CHANGE this to the actual server IP)
server_ip = "127.0.0.1"  # Use LAN/WAN IP of the server
port = 12345

# SSL Context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # Ignore certificate verification (optional)

# Connect securely
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(client_socket, server_hostname=server_ip)

secure_socket.connect((server_ip, port))
print(f"[+] Connected securely to {server_ip}:{port}")

while True:
    # Take command input
    command = input("Shell> ")
    if command.lower() == "exit":
        break  # Exit if user types 'exit'

    secure_socket.send(command.encode())  # Send command

    # Receive response
    response = secure_socket.recv(4096).decode()
    print(response)

secure_socket.close()
print("[-] Connection closed.")

