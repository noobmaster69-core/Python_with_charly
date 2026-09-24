# Lo que he estado aprendiendo en python.

## Variables 
_Aprendi que son las variables y como almacenar  informacion en ellas. 
También que para nombrar variables se deben seguir algunas normas_:

- Usar palabras en inglés.
- Se pueden utilizar letras, números y guion bajo `_`.
- No comenzar el nombre con un número.
- No usar espacios.
- No usar palabras reservadas de python.
## strings
_Strings es una cadena de caracteres y que se puede escribir utilizando comillas simples `' '` o dobles `" " `_.
 
 POR EJEMPLO: 
 ```python
message = "Hola amigo Python"
print(message)
```
---
## metodos de strings
### son los que me permiten modificar la forma en que se muestra un texto.
- name.title()
- name.upper()
- name.lower()
--- 
## COMENTARIOS
_Los # sirven para escribir comentarios en python. Solo sirven para para explicar código y pues python no los ejecuta_.

Ejemplo:

```python
# mi nombre es cristianzx
message = "soy aprendiz de charly" 
print(message)
```
## Concantenacion de strings 
_Sirve para unir dos o mas strings.
Se puede realizar utilizando el operador `+`_.

Ejemplo:
```python
first_name = "crixs"
last_name = "Eduardo"
full_name = first_name + " " + last_name 
print(full_name)
```
---
## Whitespace
_Son los espacios o caracteres utilizados para organizar el texto_.

Por ejemplo: \t agregar una tabulacion y \n realiza un salto de linea 
```python 
print("Hola\tcrixs")
print("Hola\ncrixs")
\t- tabulacion
\n- salto de linea 
```
## F-strings
_Son los que me permiten insertar variables directamente dentro de un string. Para usarlo se pone una `f` antes de las comillas y variables se escriben en {}_.

Por ejemplo:
```python 
name = "Cristian"
age = 18

message = f"Mi nombre es {name} y tengo {age} años."
print(message)
```
---
## Metodo .join()

_Sirve para unir varios strings de una lista (u otra variable) usando un separador que yo elija_.
```python
# Sintaxis
"Sepador".join(iterable)

Ejemplo: 
palabras = ["Hola","mundo","Python"]
resultado = " ".join(palbras)
print(resultado)

resultado: Hola mundo python

# Tipos de separadores
- print(" ".join(palabras))
- print("-".join(palbras))
- print(", ".join(palbras))
```
---
## SyntaxError
_Es para identificar y comprender los errores de sintaxis(Syntaxerror) que aparecen cuando escribimos codigo de python de manera incorrecta_.

Por ejemplo:
```python
if edad >= 18
print("Mayor de edad")

Ahí le falto ":"  despues de la condicion.
La forma correcta es:

if edad >= 18:
    print("Mayor de edad")
```
---
## Understandig numbers
_Aprendi sobre el manejo de números en python, en la clase vimos números enteros(int) y decimales(float), ademas de realizar operaciones_.

Ejemplo:
```python
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2)

resultado:

5
1
6
1.5
15
```
---

