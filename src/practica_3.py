
"""
vamos a realizar un programa que pregunte 
el nombre de una persona

"""
name = input("¿Como te llamas?")
age_txt = input("¿Cual es tu edad?")

try:
    age = int(age_txt) #Convierte string a int 
except:
    print("Solo se aceptan edades enteras.")
    print("Por favor, no ingreses caracteristicas alfabeticos o síbolos.")
    raise SystemExit(1)

print(f"Hola{name}, Tienes {age_txt} años.")
print("En Korea tendrias", age+1)


print("Procesos posteriores")