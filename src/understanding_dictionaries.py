"""

    Diccionarios
    
"""
# How to access to a dictionary element
covenant_elite = {'color': "blue", 'points': 10}
print(covenant_elite)

print(covenant_elite['color'])
print(covenant_elite['points'])


# How to add elements to a dictionary
covenant_elite['x-position'] = 0
covenant_elite['y-position'] = 25
covenant_elite['weapon'] = "sword"
print(covenant_elite)

# Empty Dictionary
covenant_grunt = {}
print(type(covenant_grunt))

covenant_grunt['color'] = 'orange'
covenant_grunt['points'] = 1
print("Covenan Grunt", covenant_grunt)

covenant_grunt['points'] = 5
print("Covenan Grunt", covenant_grunt)

del covenant_grunt['points']
print(covenant_grunt)


covenant_grunt['x-position'] = 5
covenant_grunt['y-position'] = 25
covenant_grunt['speed'] = 'medium'

print(covenant_grunt)

if covenant_grunt['speed'] == 'slow':
    x_increment = 1
elif covenant_grunt['speed'] == 'medium':
    x_increment = 10
else:
    x_increment = 20

covenant_grunt['x-position'] = \
    covenant_grunt['x-position'] + \
    x_increment

print(covenant_grunt)


programming_lenguages = {
    'alan': 'c++', 
    'chuy': 'python',
    'victor': 'javascrip',
    'gil': 'python',
    'mau': 'c',
    'cesar': 'javascrip',
}
print(programming_lenguages['alan'].title())

for key, value in programming_lenguages.items():
    print(f"{key.title()} le gusta el lenguage:", value)


"""
    Keys
"""
friends = ['gil', 'angel']
for name in programming_lenguages.keys():
    if name in friends:
        print(f" {name} Hola es un gusto saber que te gusta: {programming_lenguages[name]}" )

if 'charly' not in programming_lenguages.keys():
    print("A charly no le gusta programar")
    
print(programming_lenguages.keys())

for key in programming_lenguages.keys():
    print(key)

print()

for key in sorted(programming_lenguages.keys()):
    print(key)

# set() para conjuntos {}
# dict() para diccionarios {"key": value}
# list() para listas
# tuple() para tuplas
print()    
print()    
print()    
print("\n\n Clase de Conjuntos \n\n")
print(programming_lenguages)
print(" TOdos los valores ")    
for lenguaje in programming_lenguages.values():
    print(lenguaje)    
print()

print(" Set ")    
for lenguaje in set(programming_lenguages.values()):
    print(lenguaje)
    """
    Nesting - Dictionaries in Lists
"""
covenant_elite = {'color': 'blue', 'puntos': 10}
covenant_jackal = {'color': 'gray', 'puntos': 8}
covenant_grunt = {'color': 'orange', 'puntos': 5}

covenants = [covenant_elite, covenant_jackal, covenant_grunt]

print("Covenants")
print(covenants)

for covenant in covenants:
    print(covenant)
    
# Vamos a crear una flotilla de 30 covenants gruts
covenant_fleet = []
for _ in range(30):
    new_covenant ={'color': 'orange', 'puntos': 5}
    covenant_fleet.append(new_covenant)
    
print(covenant_fleet)
print(len(covenant_fleet))

"""
    Listas en Diccionarios
"""
# Menú
tacos = {
    "tortillas": ['harina', 'maiz'],
    "guisos": ['bistek', 'tripa', 'pastor'],
}

print("Tu has ordenado unos tacos " + 
      f"de {tacos['guisos'][0]} en tortilla de {tacos['tortillas'][0]}")

## Imprimir los lenguales de cada persona
favorite_games = {
    "charly": ['fornite', 'halo', 'gearsofwar'],
    "alan": ['apex', 'warzone', 'counterstrike'],
    "valente": ['minecraft', 'rocketleague', 'blasphemous'],
    'doria': ["valorant", 'blackops'],
}

for name, games in favorite_games.items():
    print(name)
    for game in games:
        print("\t"+game.title())
        
        
"""
    Dictionaries in dictionaries
"""
# Caso de uso Usernames en una aplicación web
users = {
    "charlymercury": {
        "firstname": "Carlos",
        "lastname": "Tovar",
        "age": 32,
        "height": 175,
    }, 
    "maugmr": {
        "firstname": "Mauricio",
        "lastname": "Ramos",
        "age": 18,
        "height": 165,
    }, 
    "boliche717171": {
        "firstname": "Eduardo",
        "lastname": "Zayas",
        "age": 18,
        "height": 182,
    }, 
}

for user, user_info in users.items():
    print(user)
    full_name = user_info['firstname'] + " " + user_info['lastname']
    print("\t ",full_name, "tiene: ", f"{user_info['age']} años.", " Y mide: " + str(user_info['height']))
    
"""
    Request an api ->  pip install requests
    Petición a una API
"""
