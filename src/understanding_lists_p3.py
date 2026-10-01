
# Trabajando con listas 
print("\n\tel dia de hoy voy a trabajar con las listas\n".upper())
# Vamos a crear una lista de puros strings
magicians = ['harry','ron','hermione','snape','voldemor']
print(magicians)

print("imprimir a la mala")
print(magicians[0], magicians[1],magicians[2],magicians[3],magicians[4])



# ciclo for
print("imprimir con un for")
for gato in magicians:
  print(gato, end=" ")

  # A esto se le conoce como looping
  # for cat in cats
  # for dog in dogs
  # for item in items
  # magicians = ['harry','ron','hermione','snape','voldemor']}
  # Ahora un mensaje para cada mago

for magician in magicians:
  print(f'{magician.title()} ese fue un gran hechizo')
  print(f'no puedo esperar a ver el siguiente hechizo,{magician.upper()}\n')
print("gracias a todos. Fue un gran espectaculo")