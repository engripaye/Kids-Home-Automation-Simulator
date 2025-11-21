from sqlalchemy.orm import Session
import models
import schemas


def get_devices(db: Session):
    return db.query(models.Device).all()
