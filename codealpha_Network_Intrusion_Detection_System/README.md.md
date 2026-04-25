# Network Intrusion Detection System (NIDS) Home Lab

## 📌 Project Overview
This repository documents the creation of a network monitoring environment. The goal is to simulate an attack-defense scenario where a Kali Linux machine scans a Windows-based HTTP server, and a Network Intrusion Detection System (NIDS) identifies the activity.

## 🛠️ Lab Architecture
* **Target:** Windows 11 Host running a mock HTTP server.
* **Attacker:** Kali Linux VM on the same virtual subnet (`192.168.196.0/24`).
* **Objective:** Detect unauthorized service discovery and vulnerability scanning.

## 🚀 Implementation Steps

### Step 1: Setting up the Vulnerable Service
I configured the **Everything** search utility to run an HTTP server on Port 80. This simulates a web-facing service that an attacker might target.
![HTTP Server Setup](./screenshots/WINDOWS%20MACHINE%20SET%20AS%20A%20HTTP%20SERVER.png)

### Step 2: Network Reconnaissance
Using Nmap from the Kali machine, I performed a service version detection scan (`-sV`) and used the `http-waf-detect` script to fingerprint the server.
* **Command:** `sudo nmap -sT -sV -p80 --script http-waf-detect 192.168.196.1`
* **Finding:** The scan successfully identified the "Everything HTTP Server" and the 404 response headers.
![Nmap Scan](./screenshots/NMAP%20IP-PORT.jpg)

### Step 3: Network Configuration
To ensure proper traffic capturing, I verified the virtual network adapters. The communication happens over the `VMnet8` adapter on the `192.168.196.x` subnet.
![IP Config](./screenshots/WINDOWS%20IPCONFIG.jpg)

## 🛡️ IDS Configuration (Snort/Suricata)
To detect the Nmap scan shown above, the following Snort rule is implemented to alert on Nmap's default User-Agent or rapid connection attempts:

```bash
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"NMAP HTTP Scan Detected"; content:"Nmap"; http_header; sid:1000001; rev:1;)