from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "pH Susu Sapi IoT", "status": "running"}
