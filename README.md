Here is the **README** file for your **TCP and UDP Client-Server Implementation**, fulfilling all the required criteria:  

---

# TCP and UDP Client-Server Communication  

## Overview  
This implements a **TCP-based** and **UDP-based** client-server application to analyze and compare their performance in terms of **latency, reliability, and throughput**.  

## Implementation Details  

### 1. TCP Server  
- Listens for incoming TCP connections.  
- Responds with `"Received: <message>"`.  
- Measures the **round-trip time (RTT)** for each message.  

### 2. TCP Client  
- Sends **100 messages sequentially** to the server.  
- Records the **round-trip time (RTT)** for each message.  
- Calculates **average latency and throughput**.  

### 3. UDP Server  
- Listens for incoming UDP packets.  
- Simulates **packet loss** by randomly dropping packets.  
- Responds with `"Received: <message>"` for non-dropped packets.  

### 4. UDP Client  
- Sends **100 messages sequentially** to the server.  
- Tracks **round-trip time and packet loss**.  
- Calculates **average latency, packet loss rate, and throughput**.  

---

## **Comparison and Analysis**  

### 1. **Latency Comparison**  
- **RTT for TCP and UDP is logged and compared.**  
- **Why does UDP have lower latency than TCP?**  
  - UDP has **no connection setup** and **no acknowledgment overhead**, making it faster than TCP.  

### 2. **Reliability and Packet Loss**  
- **What happens when some UDP packets are lost?**  
  - They are **not retransmitted**, leading to possible data loss.  
- **Why does TCP ensure all packets arrive correctly?**  
  - TCP uses **acknowledgments and retransmissions** to ensure data integrity.  

### 3. **Throughput Analysis**  
- **Which protocol is faster for bulk data transfer?**  
  - **UDP is faster** due to less overhead.  
- **Why does TCP introduce overhead due to acknowledgments?**  
  - TCP requires **ACK packets** and maintains an **orderly stream**, which adds delay.  

### 4. **Use Cases**  
- **When should an application use TCP instead of UDP?**  
  - **Use TCP** when **reliability is critical** (e.g., HTTP, file transfer, emails).  
  - **Use UDP** when **speed is preferred over reliability** (e.g., VoIP, online gaming, video streaming).  

---

## **How to Run the Programs**  

### **TCP Server**  
```
python tcp_server.py
```
### **TCP Client**  
```
python tcp_client.py
```
### **UDP Server**  
```
python udp_server.py
```
### **UDP Client**  
```
python udp_client.py
```

---

## **Expected Output**  
The **log files** contain the real execution outputs for **TCP and UDP tests**.  

- **TCP logs:** `tcp_server_output.txt`  
- **UDP logs:** `udp_client_output.txt`  

These files record **latency, packet loss, and throughput** results.  

---

## **References**  
- **GeeksforGeeks**: TCP vs UDP comparison  

---
