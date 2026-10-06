

"""
    La listas también pueden almacenar números y son ideales para 
    almacenarlos. Python ofrece cantidades de herramientas que ayudan a 
    trabajar eficientemente con listas de números.
"""

# Método built-in Range()
# El método range nos ayuda a crear fácilmente series de números
# Ejemplo:
for value in range(1, 5):
    print(value)

# Crear una lista de números utilizando range
numbers = list(range(-1, 11))
# Invertir una lista    
numbers.reverse()
print(numbers)

# Crear una lista de números utilizando range
first_ten_numbers = range(0,10)
# print(type(first_ten_numbers))
for value in first_ten_numbers:
    print(value)

for value in range(1,6):
    print(value)

# lista de numeros pares 
even_numbers = list(range(0,11,2))
print(even_numbers)

# ejecicio
even_numbers = list(range(5,51,5))
print(even_numbers)

