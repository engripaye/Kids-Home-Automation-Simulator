from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str
    type: str


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int
    state: bool

    class Config:
        orm_mode = True
