from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ph import router as ph_router
from databases.db import Base, engine
import uvicorn


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

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0")
