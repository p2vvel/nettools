import ipaddress
from typing import Iterator
from scapy.all import srp, Ether, ARP
import concurrent.futures
import socket
import re
import subprocess


# TODO change list[str] and tuple[boole etc.] to 
# from typing import List
# from typing import Tuple
# List[str]

def ping_host(address: str) -> list[str]:
    """Execute ping command

    Args:
        address (str): host address (e.g. "192.168.1.1")

    Returns:
        list[str]: list of addresses of detected hosts
    """
    try:
        subprocess.check_output(["ping", "-w", "1", "-c", "1", address])
        return True
    except Exception as e:
        # host didn't respond to ping
        print(e)
        return False
    

def scan_hosts_ARP(network_address: str, timeout: int = 5) -> list[str]:
    """Scan the network for hosts using ARP

    Args:
        network_address (str): _description_
        timeout (int, optional): parameter specifying how accurate is scanning process. Defaults to 5.

    Returns:
        list[str]: list of hosts in the given network
    """
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /
                     ARP(pdst=network_address), timeout=timeout, verbose=False)
    return [r.psrc for p, r in ans]


def scan_hosts_ICMP(address: str, max_workers: int = 100) -> list[str]:
    """Scan the network for hosts using ICMP (ping)

    Args:
        network_address (str): _description_
        max_workers (int, optional): parameter specifying paralelism, more = faster. Defaults to 100.

    Returns:
        list[str]: list of hosts in the given network
    """
    hosts = ipaddress.ip_network(address).hosts()
    active_hosts = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for host in hosts:
            future = executor.submit(ping_host, str(host))
            if future.result():
                active_hosts.append(host)
    return active_hosts

# with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
#             for port in ports:
#                 future = executor.submit(scan_port, address, port, timeout, protocol)
#                 if future.result()[1]:
#                     open_ports.get(alias).append(future.result()[0])
    


def scan_port(address: str, port: int, timeout: float, protocol_type: socket.SocketKind = socket.SOCK_STREAM) -> tuple[bool, int]:
    """Check if port on the host is open (considering protocol type)

    Args:
        address (str): host address (e.g. "192.168.0.1")
        port (int): port
        timeout (float): parameter determining how detailed is scanning process, longer time = better scanning
        protocol_type (socket.SocketKind, optional): protocol in 4th ISO/OSI layer. Defaults to socket.SOCK_STREAM (TCP), \
            might be also socket.SOCK_DGRAM (UDP).

    Returns:
        tuple[bool, int]: result in format (True, 53) => port 53 is open
    """
    scanner = socket.socket(socket.AF_INET, protocol_type)
    scanner.settimeout(timeout)
    try:
        if protocol_type == socket.SOCK_STREAM:
            # scan for open TCP ports
            scanner.connect((address, port))
            scanner.close()
            return port, True
        elif protocol_type == socket.SOCK_DGRAM:
            # scan for open UDP ports
            scanner.sendto(f"Hello {port}", (address, port))
            scanner.settimeout(0)
    except:
        # port is closed
        return port, False


def scan_ports(address: str, ports: Iterator[int], timeout: float, max_workers: int = 100) -> dict[str, list[int]]:
    """Scan specified ports on the host

    Args:
        address (str): host address (e.g. "192.168.0.1")
        ports (Iterator[int]): ports to scan
        timeout (float): parameter determining how detailed is scanning process, longer time = better scanning
        max_workers (int, optional): parameter specifying paralelism, more = faster. Defaults to 100.

    Returns:
        dict[str, list[int]]: result e.g. {"TCP": [80], "UDP": []}  => only port 80 open on TCP, all ports closed on UDP
    """
    open_ports = {"TCP": [], "UDP": []}
    for alias, protocol in (("TCP", socket.SOCK_STREAM), ("UDP", socket.SOCK_DGRAM)):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            for port in ports:
                future = executor.submit(scan_port, address, port, timeout, protocol)
                if future.result()[1]:
                    open_ports.get(alias).append(future.result()[0])
    return open_ports


def parse_ports_config(ports_config: str) -> list[int]:
    """Parse ports config and return list of ports that should be scanned

    Args:
        ports_config (str): string containing port config

    Returns:
        list[int]: list of ports to scan
    """
    # Parse config to create list of ports to scan
    ports = []
    scopes = [k.strip() for k in ports_config.split(",")]

    for s in scopes:
        if re.match(r"^\d+$", s) and (0 <= int(s) < 2**16):
            # single numbers
            ports.append(int(s))
        elif re.match(r"\d+\s*-\s*\d+", s):
            # ports range
            values = [int(k) for k in re.findall("\d+", s)]
            if 0 <= values[0] <= values[1] < 2**16:
                ports.extend(list(range(values[0], values[1] + 1)))

    # return only unique ports
    return list(set(ports))


if __name__ == "__main__":
    network_address = "192.168.1.0/24"
    result = scan_hosts_ICMP(network_address)
    print(result)