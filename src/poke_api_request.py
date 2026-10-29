
# La api corresponde a la informacion de charizar
import requests


api_url = "https://pokeapi.co/api/v2/pokemon/6"
#Esta es la primera petician que estamoshaciendo 
response  = requests.get(api_url,timeout = 10)
# Para revisar que si hubo error en la petecion
response.raise_for_status()
# vamos a imprimir el codigo en estado
print(response.status_code)
pokemon = response.json()
# vamos a imprimir el tipo de variable 
print(type(pokemon))

print("id:",pokemon["id"])
print("nombre:",pokemon["name"])
print("altura: ",pokemon["height"]/10)