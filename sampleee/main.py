from fastapi import FastAPI
from db import init_db
from routes import Swag,User
import uvicorn

app = FastAPI()
app.include_router(Swag.router)
app.include_router(User.router)

@app.on_event("startup")
def on_startup():
    init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)