
"""
Las listas nos permitan almacenar informacion en un lugar,
la cantidad que se desee: ya sean pocos elementos
o millones de elementos.

Una lista es una coleccion de items (elementos) que tiene 
un orden particular. Se pueden crear listas que incluyan
strings, enteros, floats, los nombres de las personas de tu
familia, etc, podemos almacenar (los tipos de datos 
permitidos en python) lo que queramos en una lista.

Son elementos Mutables: pueden modificarse el tamaño de la liata.

Se recomienda nombrar una variable del tipo lista en plural.

En python, los corchetes [] indican una lista,
sus elementos se separan por comas.

Ejemplo:

"""
bicycles = ['trelk' , 'cannondale' , 'redline', 'specialized' , 'apache']
print(bicycles)

# ¿Como podemos acceder a los elementos de una lista?

"""
Las listas son colecciones ordenadas. Se puede acceder 
a un elemento de una lista diciendole a python la
 posicion o indice del elento deseado.

 Para optener el valor deseado, de debe escribir 
 el nombre de la lista, seguido del indice del elemento
 entre corchetes. 
"""
print(bicycles[0],bicycles[1],bicycles[2])
print(bicycles[0].upper())

# Los indices comienzan en 0 y no en 1 
# bbycycles = ['trelk' , 'cannondale' , 'redline', 'specialized' , 'apache']
# Ejemplo:

print(bicycles[1])#cannondale
print(bicycles[3])#specialized

# Accediendo al ultimo elemento de una lista 

print(bicycles[-1])#apache
print(bicycles[-2])#specialzed

# Utilizando valores individuales de una lista 

message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)