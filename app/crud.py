from sqlalchemy.orm import Session
import models
import schemas


def get_devices(db: Session):
    return db.query(models.Device).all()


def get_device(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()


def toggle_device(db: Session, device_id: int):
    device = get_device(db, device_id)
    if device:
        device.state = not device.state
        db.commit()
        db.refresh(device)
    return device


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(name=device.name, type=device.type)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device
