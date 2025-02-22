import socket
import requests

def is_port_open(host, port, timeout=3):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host,port))
        return result==0


#Declarations
host = '0.0.0.0'
port = 12345


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print (f"Local IP address: {local_ip}")

#public_IP
#response = requests.get("https://api64.ipify.org?format=text")
#print(f"Public IP address: {response.text}")

server_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(5)

if is_port_open(host,port):
    print(f"Port {port} is open on {host}")
else:
    print(f"Port {port} is blocked or closed on {host}")


print(f"Server listening on {host}:{port}.....")



conn,addr = server_socket.accept()

print(f"{conn}connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"recieved:{data.decode()}")
    conn.sendall(data)

conn.close()
server_socket.close()
