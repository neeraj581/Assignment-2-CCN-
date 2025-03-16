import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12346))  # Listen on all interfaces, port 12346
print("UDP Server is listening on port 12346...")
while True:
    # Receive data from client
    data, addr = server_socket.recvfrom(1024)  # Buffer size 1024 bytes
    message = data.decode().strip()
    # Simulate packet loss (drop 10% of packets)
    if random.random() > 0.1:  # 90% chance of responding
        response = f"Received: {message}".encode()
        server_socket.sendto(response, addr)
        print(f"Responded to {addr} with: {response.decode()}")
    else:
        print(f"Simulated packet loss for message: {message}")
