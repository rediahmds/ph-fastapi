from fastapi import FastAPI
from src.routes.ph import router as ph_router
from src.databases.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "pH Susu Sapi IoT", "status": "running"}

app.include_router(ph_router)
