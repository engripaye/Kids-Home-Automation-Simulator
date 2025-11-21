from sqlalchemy.orm import Session
import models
import schemas


def get_devices(db: Session):
    return db.query(models.Device).all()


def get_device(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()
