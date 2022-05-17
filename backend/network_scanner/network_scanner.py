import ipaddress
from utils import *
import yaml



class NetworkScanner:
    def __init__(self) -> None:
        self.read_config()
        try:
            # network IP address validation
            temp = ipaddress.ip_network(self.network)
        except:
            pass    # handle wrong network address


    def read_config(self) -> None:
        """
        Read and parse configuration file
        """
        try:
            # load config files
            with open("config.yaml") as config_file:
                config = yaml.safe_load(config_file)
            self.network = config.get("network", "")
            temp = config.get("port_scanner", {}).get("ports", "")
            self.ports = parse_ports_config(temp)
            self.port_timeout = float(config.get("port_scanner", {}).get("timeout", "0.01"))
            self.host_timeout = float(config.get("host_scanner", {}).get("timeout", "5"))
        except:
            # use default parameters
            self.network = ""   # raise validation error later
            self.host_timeout = 5
            self.port_timeout = 0.01
            self.ports = list(range(2**16))     # ports in range <0, 2**16 - 1>


    def detect_hosts(self) -> None:
        """
        Find hosts in the network
        """
        available_hosts_ARP = scan_hosts_ARP(self.network, self.host_timeout)
        available_hosts_ICMP = scan_hosts_ICMP(self.network, self.host_timeout)
        self.available_hosts = set(available_hosts_ARP + available_hosts_ICMP)

    def detect_open_ports(self) -> None:
        """
        Look for open ports at hosts found in the network
        """
        self.open_ports = {host: {} for host in self.available_hosts}
        for i, host in enumerate(self.available_hosts):
            print(f"Scanning: {host}")
            temp = scan_ports(host, self.ports, self.port_timeout)
            self.open_ports[host] = temp



if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.detect_hosts()
    print(f"Hosty: {scanner.available_hosts}")

    scanner.detect_open_ports()
    print(f"Porty: {scanner.open_ports}")

