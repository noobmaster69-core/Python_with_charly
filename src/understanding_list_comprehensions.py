
"""
   una list comprehensions cambina
   el for loop y la creacion de nuevos elementos
   en una sola linea y automaticamente agregar
   cada nuevo elemento a la lista, es decir,
   sin autorizar el metodo append.
"""
scuares = [value**2 for value in range(1,11)]
print(scuares)

names = ["Reanata, Sebas, Leo, Chico del abanico"]

names_upv = [name +" upv" for name in names]
print(names_upv)