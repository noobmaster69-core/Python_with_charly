'''
Ejercicio 
Realizar un programa que determinar el costo 
de un boleto a partir de las siguientes condiciones
- costo para 
'''
print("ingresa tu edad".title)
age = input(" ingresa tu edad:")
print(age)
print(type(age))
age = int(age)
print(type(age))

if age < 4 and age < 4:
    cost = 0

if age > 4 and age <18:
    cost = 200

if age > 18:
    cost = 500

print(f"El costo del boleto es: {cost}")

# bloque if- elif-else
if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0

print("bloque if-elif-else")
print(f"El costo del boleto es: {cost}")