import json
import ipaddress

from fastapi import FastAPI
from .utils import *
import yaml
import requests


url = 'http://localhost:80'

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

    def save_hosts(self) -> None:
        """
        Post hosts
        """
        db_hosts = requests.get(url+'/hosts/').json()
        db_hosts_ids = {}
        for host in db_hosts:
            db_hosts_ids[host['ip_address']] = host['id']
        
        print(f"host id {db_hosts_ids}")
        db_hosts = [host_in_db["ip_address"] for host_in_db in db_hosts]
        
        hosts_to_add    = self.available_hosts - set(db_hosts)
        hosts_to_remove = set(db_hosts) - self.available_hosts

        print(f"host to add {hosts_to_add}")
        print(f"host to remove {hosts_to_remove}")
        for host in hosts_to_add:
            payload = {"name": host, "ip_address": host}
            r = requests.post(url+'/host/', data=json.dumps(payload))

        for host in hosts_to_remove:
            r = requests.delete(f"{url}/host/{db_hosts_ids[host]}")


    def save_ports(self) -> None:
        for host in self.open_ports:            
            host_id = requests.get(f"{url}/hosts?ip_address={host}").json()
            host_ports_tcp = []
            host_ports_udp = []
            for port in host_id['ports']:
                if port['proto'] == False:
                    host_ports_tcp.append(port['number_of_port'])
                else:
                    host_ports_udp.append(port['number_of_port'])
            host_id = host_id['id']
            
            for tcp_port in self.open_ports[host]['TCP']:
                if tcp_port not in host_ports_tcp:
                    payload = { "number_of_port": tcp_port, "proto": False, "host_id": host_id}
                    r = requests.post(url+'/hosts/ports/', data=json.dumps(payload))                
            
            for udp_port in self.open_ports[host]['UDP']:
                if udp_port not in host_ports_udp:
                    payload = { "number_of_port": udp_port, "proto": True, "host_id": host_id}
                    r = requests.post(url+'/hosts/ports/', data=json.dumps(payload))                


if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.detect_hosts()
    print(f"Hosty: {scanner.available_hosts}")

    scanner.detect_open_ports()
    print(f"Porty: {scanner.open_ports}")

