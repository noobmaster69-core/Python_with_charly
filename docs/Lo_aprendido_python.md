# Lo que he estado aprendiendo en python.

## Variables 
Aprendi que son las variables y como almacenar  informacion en ellas. 
También que para nombrar variables se deben seguir algunas normas:

- Usar palabras en inglés.
- Se pueden utilizar letras, números y guion bajo `_`.
- No comenzar el nombre con un número.
- No usar espacios.
- No usar palabras reservadas de python.
## strings
Strings es una cadena de caracteres y que se puede escribir utilizando comillas simples `' '` o dobles `" " `.
 
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
Los # sirven para escribir comentarios en python. Solo sirven para para explicar código y pues python no los ejecuta.

Ejemplo:

```python
# mi nombre es cristianzx
message = "soy aprendiz de charly" 
print(message)
```
## Concantenacion de strings 
Sirve para unir dos o mas strings.
Se puede realizar utilizando el operador `+`

Ejemplo:
```python
first_name = "crixs"
last_name = "Eduardo"
full_name = first_name + " " + last_name 
print(full_name)
```
---
## Whitespace
Son los espacios o caracteres utilizados para organizar el texto.

Por ejemplo: \t agregar una tabulacion y \n realiza un salto de linea 
```python 
print("Hola\tcrixs")
print("Hola\ncrixs")
\t- tabulacion
\n- salto de linea 
```
## F-strings
Son los que me permiten insertar variables directamente dentro de un string. Para usarlo se pone una `f` antes de las comillas y variables se escriben en {}.

Por ejemplo:
```python 
name = "Cristian"
age = 18

message = f"Mi nombre es {name} y tengo {age} años."
print(message)
```

