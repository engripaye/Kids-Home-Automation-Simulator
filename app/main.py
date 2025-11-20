from fastapi import FastAPI
from app.routers import devices
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kids Home Automation Simulator")