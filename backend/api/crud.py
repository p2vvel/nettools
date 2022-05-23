from ipaddress import ip_address
from sqlalchemy.orm import Session

from . import models, schemas


def get_host(db: Session, host_id: int):
    return db.query(models.Hosts).filter(models.Hosts.id == host_id).first()


def get_host_by_ip(db: Session, ip_address: str):
    return db.query(models.Hosts).filter(models.Hosts.ip_address == ip_address).first()


def get_hosts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hosts).offset(skip).limit(limit).all()


def create_host(db: Session, host: schemas.HostsCreate):
    db_host = models.Hosts(name=host.name, ip_address=host.ip_address)
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    return db_host


def update_host_name(db: Session, host_id: int, new_name: str):
    host = get_host(db, host_id)
    host.name = new_name
    db.commit()
    

def get_host_ports(db: Session, host_id: int):
    return db.query(models.Ports).filter(models.Ports.host_id == host_id).all()


def create_host_ports(db: Session, port: schemas.PortsCreate):
    p = models.Ports(**port.dict())
    db.add(p)
    db.commit()
    return p


def delete_host(db: Session, host_id: int):
    host_to_delete = db.query(models.Hosts).filter(models.Hosts.id == host_id).first()
    db.delete(host_to_delete)
    db.commit()