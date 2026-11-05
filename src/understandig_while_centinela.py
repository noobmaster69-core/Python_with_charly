
"""
while - sentinel - centinela 
while True:
  print("hola)

Realizar un programa que capture el
importe y que acumele todos éstos importes 
en una variable 
"""
sum = 0.0
message = """
Sistema gestor de acumlacion de valores
La creativador esta en tus manos.

En todo el momento, si quieres salir del programa 
puedes tipear q, e, quit, exit

Ingresa un valor: """

while True:

    value_txt = input(message)

    if value_txt == 'quit' or \
    value_txt == "exit" or \
    value_txt == "e" or \
    value_txt == "q":
        break


try:

    value = float(value_txt)
    sum += value
except ValueError:
    print("Ingresaste un dato no valido.") 

print(f"Tu valor acumulado es: {sum}")

total = 0.0
counter = 0
minimun = None
maximun = None

while True:
    value_txt = input("Igresa un valor o 'q', 'e', 'quit', 'exit'").lower().replace(" ", " ")
    if value_txt  in ['quit', 'e', 'quit', 'exit']:
        break

    try:
        value_txt = float(value_txt)
    except ValueError:
        print("dato ingresado no dado.")

total += value
counter += 1

if minimun is None or value < minimun:
    minimun = value
    if maximun is None or value > maximun:
        maximun = value
        if counter

