# Combiancion o concatenación de strings
frist_name = "cristzx"
last_name = "eduardo"
full_name = frist_name + " " + last_name
print(full_name.title())

print("hola".title(),frist_name.upper() + " " + last_name.upper())

"""
# Whitespace se refiere a cualquier caracter 
que no se imprime, es decir , un espacio (),
tabuladores (\t) y fianles de linea (\n)

Los whitespace se utilizan  normalmente para
organizar las salidas de un texto a usuario
de tal manera que sea mas amigable de leer o ver
para los usuarios
"""
print("python")
print("\tpython")
print("\t\tpython")
print("lenguajes:\n\tpython\nC\nJavaScript")

# f-strings
famus_person = "crisxs"
message = f" {famus_person.upper()} una vez dijo .python is love"
print(message)