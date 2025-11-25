from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import devices
from app.database import Base, engine
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kids Home Automation Simulator")

app.include_router(devices.router)


# Serve frontend folder as static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")



@app.get("/")
def read_root():
    return FileResponse(os.path.join("frontend", "index.html"))

