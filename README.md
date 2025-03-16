### **README: TCP & UDP Client-Server Implementation**  

---

## **1. Introduction**  
This  implements **both TCP and UDP** client-server applications in Python and analyzes their performance based on **latency, reliability, and throughput**.  

---

## **2. Basic Knowledge of TCP and UDP**  

### **TCP (Transmission Control Protocol)**  
- **Connection-oriented** protocol: Establishes a reliable connection before data transfer.  
- **Ensures reliable communication**: Packets are acknowledged, retransmitted if lost, and arrive in order.  
- **Slower but reliable** due to extra processing (handshaking, error checking).  
- **Used for:** Web browsing (HTTP, HTTPS), file transfers (FTP), emails (SMTP).  

### **UDP (User Datagram Protocol)**  
- **Connectionless**: Sends packets without establishing a connection.  
- **Unreliable but fast**: No acknowledgments or retransmissions, leading to possible packet loss.  
- **Used for:** Real-time applications like VoIP, online gaming, and video streaming.  

---

## **3. Implementation**  

The project consists of **four Python scripts:**  
1. `tcp_server.py` – Listens for TCP connections and responds with "Received: <message>".  
2. `tcp_client.py` – Sends 100 messages, records RTT, and calculates average latency & throughput.  
3. `udp_server.py` – Listens for UDP packets, simulates packet loss, and responds when applicable.  
4. `udp_client.py` – Sends 100 messages, tracks RTT and packet loss rate.  

---

## **4. How to Run the Programs**  

### **Step 1: Start the Server**  
Run the **TCP Server** in one terminal:  
```bash
python tcp_server.py
```
Run the **UDP Server** in another terminal:  
```bash
python udp_server.py
```

### **Step 2: Run the Client**  
Run the **TCP Client** in a separate terminal:  
```bash
python tcp_client.py
```
Run the **UDP Client** in another terminal:  
```bash
python udp_client.py
```

### **Step 3: View Logs**  
The execution logs are stored in:  
- `tcp_log.txt` – Records TCP communication logs and RTT.  
- `udp_log.txt` – Records UDP communication logs, packet loss, and RTT.  

---

## **5. Expected Output**  

**TCP Client-Server Output (Example in `tcp_log.txt`)**  
```
[CLIENT] Sending message 1: "Hello TCP Server"
[SERVER] Received: "Hello TCP Server"
[CLIENT] Response received: "Received: Hello TCP Server" | RTT: 10ms

Total messages sent: 100
Average Latency: 11ms
Throughput: X messages/sec
```

**UDP Client-Server Output (Example in `udp_log.txt`)**  
```
[CLIENT] Sending message 1: "Hello UDP Server"
[SERVER] Received: "Hello UDP Server"
[CLIENT] Response received: "Received: Hello UDP Server" | RTT: 8ms

[CLIENT] Sending message 2: "Test Packet"
[SERVER] Simulated Packet Loss (Message Dropped)
[CLIENT] No response received (Packet Lost)

Total messages sent: 100
Total packets lost: 10
Packet loss rate: 10%
Average Latency: 9ms
Throughput: X messages/sec
```

---

## **6. Comparison and Analysis**  

### **1. Latency Comparison**  
- **UDP has lower latency than TCP** because it does not wait for acknowledgments or retransmissions.  
- TCP introduces extra delay due to **three-way handshake** and **error checking**.  

### **2. Reliability and Packet Loss**  
- **UDP does not guarantee delivery**, so some packets may be lost.  
- **TCP guarantees delivery** by retransmitting lost packets and ensuring packets arrive in order.  

### **3. Throughput Analysis**  
- **UDP is faster for bulk data transfer** because it has no overhead from handshakes or acknowledgments.  
- **TCP has lower throughput** due to extra processing, but ensures data integrity.  

### **4. Use Cases**  

| Protocol | When to Use | Real-World Example |
|----------|------------|--------------------|
| **TCP** | When reliability is required | Web browsing (HTTP, HTTPS), Emails (SMTP), File transfers (FTP) |
| **UDP** | When speed is more important than reliability | VoIP (Skype, Zoom), Live video streaming (YouTube, Twitch), Online gaming |

---

## **7. References**  
To understand the concepts of TCP and UDP, we referred to the following online resources:  
- **GeeksforGeeks** – [TCP vs UDP](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/)  
- **Python Socket Programming** – [GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/)  

---

## **8. Summary of Accomplishments**  
- Implemented **TCP and UDP client-server models** in Python.  
- Measured **latency, throughput, and packet loss** using log files.  
- Compared **TCP vs. UDP performance** for different network conditions.  
- Documented results and analysis in this **README**.  

---

This README provides a complete guide to running and analyzing the TCP & UDP implementations. 🚀 Let me know if you need further modifications! 😊
