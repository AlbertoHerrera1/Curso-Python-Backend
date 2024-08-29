import requests

URL_BASE = "http://127.0.0.1:8000"

def get_usuario():
    respuesta = requests.get(URL_BASE + "/usuario/2")
    print(respuesta.json())

def put_favorito():
    respuesta = requests.put(URL_BASE + "/usuario/favorito",
                            params={"nombre": "Bistec", 
                                    "ultima_fecha": "21 de agosto de 2024",
                                    "id": 1})
    print(respuesta.json())

if __name__ == "__main__":
    # get_usuario()
    put_favorito()