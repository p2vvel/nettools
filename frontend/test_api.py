from random import randint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    result = {host: {"tcp": None, "udp": None} for host in hosts}
    return {"hosts": result}

