"""
Realizar una funcion quee genere el nombre de una 
persona, dados su : primer nombre, segundo nombre 
y apellido

"""
def create_fullname(firstname: str, lastname: str, middlename: str = "") -> str:
    """
    Esta funcion general el nombre completo de una persona
    dado los parametros.
    """

    if middlename == "":
        full_name = f"{firstname} {lastname}".title()
    else:
        full_name = f"{firstname} {middlename} {lastname}".title()
        return full_name

create_fullname("Cristian","Eduardo","Moreno Heranandez")

# Keyword Argument 
fullname_1= create_fullname(lastname ="Moreno Hernandez", firstname="Cristian", middlename="Eduardo")
print(fullname_1)
# Maxing Positional &  Keyword Argument
#create_fullname("Cristian", "Eduardo", lastname="Moreno Hernandez")

# Optional Arguments
#create_fullname("Carlos")
