from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


# TODO
# here start process of network_scanning
#

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


@app.get("/hosts/", response_model=List[schemas.Hosts])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hosts = crud.get_hosts(db, skip=skip, limit=limit)
    return hosts


@app.get("/hosts/{host_id}", response_model=schemas.Hosts)
def read_host(host_id: int, db: Session = Depends(get_db)):
    db_host = crud.get_host(db, host_id=host_id)
    if db_host is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_host

@app.post("/host/", response_model=schemas.Hosts)
def create_user(host: schemas.HostsCreate, db: Session = Depends(get_db)):
    db_host = crud.get_host_by_ip(db, ip_address=host.ip_address)
    if db_host:
        raise HTTPException(status_code=400, detail="Hosts already exists")
    return crud.create_host(db=db, host=host)


@app.post("/hosts/{host_id}/ports/", response_model=schemas.Ports)
def create_ports_for_host(
    host_id: int, port: schemas.PortsCreate, db: Session = Depends(get_db)
):
    return crud.create_host_ports(db=db, port=port, host_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


#jeszcze to 
# def get_host_by_ip(db: Session, ip_address: str):
#     return db.query(models.Hosts).filter(models.Hosts.ip_address == ip_address).first()
