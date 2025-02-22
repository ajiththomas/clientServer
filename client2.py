import socket

# Server details
server_ip = "192.168.1.1"  # Change to the actual server IP
port = 12345

# Create socket and connect
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

# Send message
client_socket.send("Hello from Client!".encode())

# Receive response from server
response = client_socket.recv(1024).decode()
print(f"[Server]: {response}")

client_socket.close()  # Close connection
