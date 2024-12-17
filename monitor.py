import socket
import struct
from collections import defaultdict

class DDOSTrafficMonitor:
    def __init__(self):
        self.packet_counts = defaultdict(int)
        self.stop_monitoring = False

    def sniff_packets(self):
        try:
            sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
            sniffer.bind(("0.0.0.0", 0))
            sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

            print("Monitoring traffic for DDoS...")
            while not self.stop_monitoring:
                packet = sniffer.recvfrom(65565)[0]
                ip_header = packet[0:20]
                iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
                src_ip = socket.inet_ntoa(iph[8])
                self.packet_counts[src_ip] += 1

            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        except Exception as e:
            print("Error: {}".format(e))

    def start_monitoring(self):
        self.sniff_packets()
