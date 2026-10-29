
"""
Programa para calcular el indice 
de la masa corporal de una persona

wheigth: peso de la persona
heigth: altura de la persona
"""
wheigh_txt = input(" Peso (kg): ")
heigh_txt =  input("Altura (mts): ")

try: 
    wheigh_txt = float(wheigh_txt)
    heigh_txt = float(heigh_txt)
    imc = wheigh / (heigh ** 2)
    print(f"Tu indice de masa corporal es {ims}")
except TypeError:
    print("Datos no validos. Ej peso 70.5, altura 1.75")
except ZeroDivisionError:
    print("La altura debe de ser diferente de cero")
except Exception:
    print(Exception)

print("procesos posteriores")