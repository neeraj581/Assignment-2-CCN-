import socket
import time
NUM_MESSAGES = 100  
# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))  # Connect to server
total_latency = 0  # Total round-trip time for all messages
for i in range(NUM_MESSAGES):
    message = f"Message {i}".encode()
    start_time = time.time()  # Start time 
    client_socket.sendall(message)  # Send the message
    response = client_socket.recv(1024).decode()  # Receive 
    end_time = time.time()  # End time
    round_trip_time = end_time - start_time  # Calculate RTT
    total_latency += round_trip_time  # total latency
    print(f"Sent: {message.decode()}, Received: {response}, RTT: {round_trip_time:.6f} sec")
average_latency = total_latency / NUM_MESSAGES
print(f"\nAverage Round-Trip Time (RTT): {average_latency:.6f} sec")
# Calculate throughput
throughput = NUM_MESSAGES / total_latency
print(f"Throughput: {throughput:.2f} messages per second")
client_socket.close()  
