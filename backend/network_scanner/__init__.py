import time
from .network_scanner import NetworkScanner


class NetworkScannerRunner: 
    @staticmethod
    def run():
        scanner = NetworkScanner()
        while True:
            scanner.detect_hosts()
            print(f"Hosty: {scanner.available_hosts}")
            scanner.save_hosts()
            scanner.detect_open_ports()
            scanner.save_ports()
            print(f"Porty: {scanner.open_ports}")
            time.sleep(10)