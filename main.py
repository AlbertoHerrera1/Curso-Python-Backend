from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_base():
    return {"Mensaje": "Hola Mundo"}