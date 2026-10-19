guisos = ['salsa verde', 'deshebrada']
if 'picadillo' in guisos:
    print("Hay Salsa verde")
elif 'picadillo' in guisos:
    print("Hay deshebrada")
elif 'chicharron' in guisos:
    print("Hay chicharron")  
else:
    print("No hay ningún guiso")  
    

# Empty List
guisos = []
if guisos:
    print("Hay elementos")
else:
    print("No hay elementos")
    

# 
guisos_disponibles = ['salsa verde', 'deshebrada', 
                      'picadillo', 'huevo con chorizo']
guisos_a_ordenar = ['chicharron', 'deshebrada', 'huevo con chorizo']
print("¿Qué guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Si tengo ese guiso: {guiso}")
    else:
        print(f"No tengo ese guiso: {guiso}")

