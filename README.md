# **DDoS Traffic Monitor**

A **real-time traffic monitoring tool** that detects and displays network traffic volume per IP address to identify potential **DDoS attacks**. The tool is built with **Python 2.7** using Flask as the backend and a web-based frontend for visualization.

---

## **Features**
- **Real-time Monitoring**: Captures network packets and displays the number of packets per IP address.
- **Web-based Dashboard**: A user-friendly interface accessible via a web browser.
- **Interactive Table**: Automatically updates every few seconds to reflect live traffic.
- **Customizable**: Can be extended to add alerts, logs, or more detailed traffic analysis.
- **Lightweight**: Uses raw sockets for packet capture and a minimal Flask server for serving data.

---

## **How It Works**
1. **Traffic Capture**: The tool uses raw sockets to sniff incoming IP packets.
2. **Data Aggregation**: It counts packets per source IP to identify potential spikes in traffic.
3. **Visualization**: Data is served via a Flask API and displayed in an HTML table that auto-updates every 2 seconds using JavaScript.

---

## **Requirements**
- **Python 2.7**
- **Flask** web framework
- Root/Admin access to capture packets via raw sockets

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Jenderal92/ddos-traffic-monitor.git
   cd ddos-traffic-monitor
   ```

2. **Install Flask**:
   ```bash
   pip install flask
   ```

3. **Run the Application** (requires root privileges):
   ```bash
   sudo python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## **Project Structure**

```
DDoS_Traffic_Monitor/
│
├── app.py                # Flask backend server
├── monitor.py            # Core packet capture and counting logic
├── templates/
│   └── index.html        # HTML dashboard
└── static/
    ├── style.css         # Styling for the dashboard
    └── script.js         # JavaScript for real-time updates
```

---

## **Usage**

1. Start the tool with:
   ```bash
   sudo python app.py
   ```

2. Open the browser and access:
   ```
   http://<server-ip>:<port>
   ```
   - Replace `<server-ip>` with your server IP address.
   - Default port is `5000`.

3. The dashboard will show:
   - **Source IP**: The IP address sending traffic.
   - **Packet Count**: Number of packets received from each IP.

---

## **Embed in a Website**

To display the tool on another website (like Blogger), use an iframe:

```html
<iframe src="http://<your-server-ip>:5000" width="100%" height="600px" frameborder="0"></iframe>
```

Replace `<your-server-ip>` with your server's IP or domain.
