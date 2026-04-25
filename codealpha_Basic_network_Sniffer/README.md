# Network Packet Analyzer 🛡️

A lightweight Python-based network sniffer that captures and analyzes real-time TCP/UDP traffic. This tool provides insights into network communication by displaying source/destination IP addresses and port numbers.

## ✨ Features
- **Real-time Sniffing:** Captures live packets from a specified network interface (Wi-Fi, Ethernet, etc.).
- **Protocol Identification:** Distinguishes between **TCP** and **UDP** traffic.
- **Port Mapping:** Extracts and displays source and destination ports for granular analysis.
- **Clean Interface:** Simplified console output with clear formatting for easy monitoring.

## 🛠️ Prerequisites
- **Python 3.x**
- **Administrative/Root Privileges:** Required to access raw network sockets.
- **Npcap (Windows):** If running on Windows, ensure [Npcap](https://npcap.com/) is installed in "WinPcap API-compatible mode."

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/network-packet-analyzer.git](https://github.com/your-username/network-packet-analyzer.git)
   cd network-packet-analyzer

## ✅ How Run
pip install -r requirements.txt
**Run the sniffer:**
Open your terminal/PowerShell as Administrator and run:
python "Sniffer Network Packet Analyzer.py"
**Select Interface:**
When prompted, enter the name of your interface (e.g., Wi-Fi or Ethernet).