from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)  # light, fan, door, fridge, calculator, gadget
    state = Column(Boolean, default=True)

