from ipaddress import ip_address
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Hosts(Base):
    __tablename__ = "hosts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip_address = Column(String)
    
    ports = relationship("Ports", back_populates= "host")

class Ports(Base):
    __tablename__ = "ports"
    id = Column(Integer, primary_key=True, index=True)
    number_of_port = Column(Integer)
    # tcp - false
    # udp - true
    proto = Column(Boolean)
    host_id = Column(Integer, ForeignKey("hosts.id"))
    host = relationship("Hosts", back_populates="ports")

