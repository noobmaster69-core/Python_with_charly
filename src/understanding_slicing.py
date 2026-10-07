players = ["peter","charly","tovar","fatima","renata"]
print("lista original: ", players)

# Slicing
print(players[3:5]) # tovar y renata
print(players[0])

# El slicing me permite trabajar con un grupo
# especifico de una lista: al resultado se le conoce como
# "un slice".
# players = ["peter","charly","tovar","fatima","renata"]

print("1:4",players[1:4])
print(":3",players[:3])
print(":.2",players[:2])
print("[-3:]",players[-3:])
print("casos especiales")


print(players)
print(players[1:10])
print(players[10:-10])
print(players[6:1])
print(players[:0])
print(players[0:1])

# Looping through a slice 
print(" Looping through a slice ")
students = ["peter","charly","tovar","fatima","renata"]

# slicing [::] Tarea

for student in students[3:5]:
    print(f"el estudiante {student}, va a pasar la materia.")

print(students)

# ¿ cmo copiar una lista ?
my_food = ["pizza"]