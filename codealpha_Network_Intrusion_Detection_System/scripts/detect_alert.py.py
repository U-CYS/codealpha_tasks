import time

LOG_FILE = "/var/log/snort/alert"

def monitor_logs():
    print("--- NIDS Real-time Monitoring Active ---")
    try:
        with open(LOG_FILE, "r") as f:
            # Go to the end of the file
            f.seek(0, 2)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                if "Nmap" in line or "Scan" in line:
                    print(f"[!] INTRUSION DETECTED: {line.strip()}")
    except FileNotFoundError:
        print("Log file not found. Ensure Snort is running.")

if __name__ == "__main__":
    monitor_logs()