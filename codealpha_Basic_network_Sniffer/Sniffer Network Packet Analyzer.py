from scapy.all import sniff, IP, TCP, UDP

def packet_sniffer(packet):
    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        
        print("\n📦 Packet Captured:")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        # Check protocol
        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        else:
            print("Protocol: Other")

def main():
    interface = input("Enter interface (e.g., Wi-Fi or Ethernet): ")
    print(f"Sniffing on {interface}...\n")
    
    sniff(iface=interface, prn=packet_sniffer, store=False)

if __name__ == "__main__":
    main()