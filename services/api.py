# contém a chamada a API do Pokédex

import requests
import json

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'
NUMBER_MAX_POKEMONS_API = 6

params = {'limit': NUMBER_MAX_POKEMONS_API}


def buscar_pokemons():
    #url = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'
    request = requests.get(BASE_URL, params)
    response = json.loads(request.content)
    return response['results']


def buscar_pokemon(url_poke):
    request = requests.get(url_poke)
    response = json.loads(request.content)
    return(response)


if __name__ == '__main__':
    import os
    os.system('clear')
    res = buscar_pokemon('https://pokeapi.co/api/v2/pokemon/1/')
    # res.data.sprites.front_default;
    print(res['types'])
    """lista = buscar_pokemons()
    print(len(lista))
    for poke in lista:
        print(f"{poke['name']} - {poke['url']}")"""


# doc requests:
#  https://docs.python-requests.org/en/latest/
#  https://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls
