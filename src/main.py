from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.ph import router as ph_router
from src.databases.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ph_router)
