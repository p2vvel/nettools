from typing import List, Union

from pydantic import BaseModel


class PortsBase(BaseModel):
    number_of_port: int
    proto: bool
    host_id: int

class PortsCreate(PortsBase):
    pass

class Ports(PortsBase):
    id: int
    class Config:
        orm_mode = True

class HostsBase(BaseModel):
    name: str
    ip_address: str

class HostsCreate(HostsBase):
    pass

class Hosts(HostsBase):
    id: int
    ports: List[Ports] = []

    class Config:
        orm_mode = True
