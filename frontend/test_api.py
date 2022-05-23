from random import randint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import sample, randint

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/fake_data/")
def read_root():
    hosts_amount = randint(1, 12)
    hosts = [f"192.168.1.{end}" for end in range(1, hosts_amount + 1)]
    ports = {20: "FTP", 21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS", 3336: "MySQL", 53: "DNS", 69: "TFTP"}
    random_ports = lambda: {k: ports.get(k) for k in sample(ports.keys(), randint(0, len(ports)))}
    result = {host: {"tcp": random_ports(), "udp": random_ports()} for host in hosts}
    return {"hosts": result}

