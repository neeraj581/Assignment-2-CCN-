import socket
import time
NUM_MESSAGES = 100  
TIMEOUT = 0.1 
server_address = ("127.0.0.1", 12346)  
# Create UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(TIMEOUT)  # Set timeout for lost packets
total_latency = 0  # Sum of all RTTs
lost_packets = 0  # Count of lost packets
for i in range(NUM_MESSAGES):
    message = f"Message {i}".encode()
    start_time = time.time()
    client_socket.sendto(message, server_address)  # Send message
    try:
        response, _ = client_socket.recvfrom(1024)  # Receive response
        end_time = time.time()
        round_trip_time = end_time - start_time
        total_latency += round_trip_time
        print(f"Sent: {message.decode()}, Received: {response.decode()}, RTT: {round_trip_time:.6f} sec")
    except socket.timeout:
        lost_packets += 1
        print(f"Sent: {message.decode()}, No response (Packet lost)")
# Compute and display average latency
successful_messages = NUM_MESSAGES - lost_packets
average_latency = (total_latency / successful_messages) if successful_messages > 0 else 0
packet_loss_rate = (lost_packets / NUM_MESSAGES) * 100
throughput = successful_messages / total_latency if total_latency > 0 else 0
print(f"\nAverage Round-Trip Time (RTT): {average_latency:.6f} sec")
print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")
print(f"Throughput: {throughput:.2f} messages per second")
client_socket.close()
