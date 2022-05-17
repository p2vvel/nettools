from typing import Iterator
from scapy.all import srp, Ether, ARP
import concurrent.futures
import socket
import re

# TODO change list[str] and tuple[boole etc.] to 
# from typing import List
# from typing import Tuple
# List[str]

def scan_hosts(network_address: str, timeout: int = 5) -> list[str]:
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /
                     ARP(pdst=network_address), timeout=timeout, verbose=False)
    return [r.psrc for p, r in ans]


def scan_port(address: str, port: int, timeout: float) -> tuple[bool, int]:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(timeout)
    try:
        scanner.connect((address, port))
        scanner.close()
        return port, True
    except:
        return port, False


def scan_ports(address: str, ports: Iterator[int], timeout: float, max_workers: int = 100) -> list[int]:
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for port in ports:
            future = executor.submit(scan_port, address, port, timeout)
            if future.result()[1]:
                open_ports.append(future.result()[0])
    return open_ports


def parse_ports_config(ports_config: str) -> Iterator[int]:
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
