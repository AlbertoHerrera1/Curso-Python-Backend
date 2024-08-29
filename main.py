from fastapi import FastAPI
from super_db import usuarios, items

app = FastAPI()

@app.get("/")
def get_base():
    return {"Mensaje": "Hola Mundo"}    


@app.get("/usuario/{id}")
def get_usuario(id: int):
    usuario = usuarios.get(id)
    if not usuario:
        return "No se encontró el usuario"
    return usuario

@app.put("/usuario/favorito")
def put_favorito(nombre: str, ultima_fecha: str, id: int):
    usuario = usuarios.get(id)
    if not usuario:
        return "No se encontró el usuario"
    usuario['favoritos'].append({
        "nombre": nombre, "ultima-fecha": ultima_fecha})
    return usuario

@app.get("/item")
def get_usuario(id: str):
    item = items.get(id)
    if not item:
        return "No se encontró el item"
    return item