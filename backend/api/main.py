from multiprocessing import Process
from typing import List
from typing import Union
from network_scanner import NetworkScannerRunner

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# fill with proper addresses/ports:
origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
def startup_event():
    p = Process(target=NetworkScannerRunner.run)
    p.start()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/hosts/", response_model=Union[List[schemas.Hosts], schemas.Hosts ])
def read_users(skip: int = 0, limit: int = 100, ip_address: Union[str, None] = None, db: Session = Depends(get_db)):
    if ip_address:
        hosts = crud.get_host_by_ip(db, ip_address)
    else:
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

@app.delete("/hosts/{host_id}" )
def delete_host(host_id: int, db: Session = Depends(get_db)):
    crud.delete_host(db, host_id)
    return {"ok": True}

@app.get("/hosts/{host_id}/ports/", response_model=List[schemas.Ports])
def get_port_for_host(host_id: int, db: Session = Depends(get_db)):
    db_host = crud.get_host(db, host_id=host_id)
    if db_host is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_host_ports(db, host_id)

@app.post("/hosts/ports", response_model=schemas.Ports)
def create_ports_for_host( port: schemas.PortsCreate, db: Session = Depends(get_db)):
    return crud.create_host_ports(db=db, port=port)

