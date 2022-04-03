from network_scanner import NetworkScanner



if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.detect_hosts()
    print(f"Hosty: {scanner.available_hosts}")

    scanner.detect_open_ports()
    print(f"Porty: {scanner.open_ports}")

