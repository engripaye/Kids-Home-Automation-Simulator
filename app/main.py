from fastapi import FastAPI
from app.routers import devices
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kids Home Automation Simulator")

app.include_router(devices.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Kids Home Automation Simulator API!"}


@app.get("/devices")
def read_device():
    return {"message": "Welcome to the Kids Home Automation Simulator API!"}