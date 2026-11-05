
""" 
Realizar un programa en el que el usuario
deba ingresar su PIN de acceso.

Si el 
"""

PIN_CORRECTO = "1234" # Pin correcto 
MAX_INTENTOS = 3 # Constante de maximos de intentos
intentos = 0
acceso = False #Bandera o flag
while intentos < MAX_INTENTOS:
    line = input("PIN (4 digitos):")

    if line == PIN_CORRECTO:
        print("Ingreso Autorizado")
        acceso = True
        break

intentos += 1 
restantes = MAX_INTENTOS - intentos

if restantes > 0:
    print(f"Pin incorrecto, intentos restantes {restantes}")
else:
    print('PIN incorrecto, cuenta bloqueada temporalmente')


if acceso:
    print("Bienvenido a la UPV")