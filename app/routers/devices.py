from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/devices")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def read_devices(db: Session = Depends(get_db)):
    return crud.get_devices(db)


@router.post("/")
def add_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db, device)


@router.post("/{device_id}/toggle")
def toggle_device(device_id: int, db: Session = Depends(get_db)):
    return crud.toggle_device(db, device_id)
