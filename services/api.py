# contém a chamada a API do Pokédex

import httpx
from qt_core import *

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'
NUMBER_MAX_POKEMONS_API = 10

params = {'limit': NUMBER_MAX_POKEMONS_API}


def buscar_pokemons():
    #request = requests.get(BASE_URL, params)
    request = httpx.get(BASE_URL, params=params)
    response = request.json()
    return response

def buscar_pokemon(url_poke):
    request = httpx.get(url_poke)
    response = request.json()
    return(response)

def loadImg(url_image):
    if url_image != "":
        img = httpx.get(url_image).content
        image = QImage()
        image.loadFromData(img)
        return QPixmap(image)
