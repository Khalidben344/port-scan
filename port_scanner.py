import socket

def scan_ports(target, start_port=1, end_port=1024):
    print(f"🔍 Scanning ports {start_port} to {end_port} on {target}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"✅ Port {port} is open")
            open_ports.append(port)
        sock.close()
    if not open_ports:
        print("❌ No open ports found.")
    else:
        print(f"\nOpen ports on {target}: {open_ports}")

if __name__ == "__main__":
    target_ip = input("🌐 Enter target IP or hostname: ")
    scan_ports(target_ip)
    input("\n🖱️ Press Enter to exit...")
