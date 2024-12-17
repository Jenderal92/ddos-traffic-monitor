from flask import Flask, render_template, jsonify
from monitor import DDOSTrafficMonitor
import threading

app = Flask(__name__)
monitor = DDOSTrafficMonitor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = [{"ip": ip, "count": count} for ip, count in monitor.packet_counts.items()]
    return jsonify(data)

def start_monitor():
    monitor_thread = threading.Thread(target=monitor.start_monitoring)
    monitor_thread.daemon = True
    monitor_thread.start()

if __name__ == "__main__":
    print("Starting DDoS Traffic Monitor...")
    start_monitor()
    app.run(debug=True, port=5000)
