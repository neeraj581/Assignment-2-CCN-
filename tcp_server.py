import socket
import time
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080)) 
server_socket.listen(5)  # Listen
print("TCP Server is listening on port 12345...")
while True:
    connection_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")
    while True:
        # Receive data from the client
        start_time = time.time()  # Start  time
        data = connection_socket.recv(4096)
        if not data:
            break  # If no data is received
          #acknowledgment back
        response = f"Received: {data.decode()}"
        connection_socket.send(response.encode())
        end_time = time.time()  # End measuring time
        round_trip_time = end_time - start_time  # Compute RTT
        print(f"Message processed. RTT: {round_trip_time:.6f} sec")
    connection_socket.close()  # 
