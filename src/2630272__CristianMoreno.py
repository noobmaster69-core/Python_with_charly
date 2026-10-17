# PORTADA

# Tarea: Colecciones en Python (listas, tuplas y diccionarios)
# Nombre: Cristian Eduardo Moreno Hernandez
# Matrícula: 2630272
# Grupo: TSU-75004


# RESUMEN EJECUTIVO
# Python tiene tres colecciones básicas: list, tuple y dict.
# Una lista guarda elementos en orden y es mutable: podemos agregar, cambiar o
# quitar elementos (append(), pop(), remove()).
# Una tupla también guarda elementos en orden pero es inmutable: una vez creada
# no se puede cambiar, por eso sirve para datos fijos como un punto (x, y).
# Un diccionario guarda pares clave -> valor, así que podemos encontrar un valor rápido
# por su clave, por ejemplo el nombre de un producto -> su precio.
# Este documento cubre seis problemas con su descripción, entradas,
# salidas, validaciones, dos casos de prueba cada uno (normal y borde)
# y el código en Python que los resuelve.


# PRINCIPIOS Y BUENAS PRÁCTICAS
# 1) Usar listas cuando los elementos se agregan o se quitan seguido.
# 2) Usar tuplas para datos que no deben cambiar (coordenadas, registros fijos).
# 3) Usar diccionarios cuando los valores se buscan por una clave (nombre -> teléfono).
# 4) Evitar modificar una lista mientras se recorre con for;
#    mejor construir una lista nueva.
# 5) Usar claves descriptivas en los diccionarios ("apple", "Alice") en lugar de
#    números sin significado.
# 6) Escribir código legible, con nombres de variables y mensajes claros.
# Nota: los booleanos se imprimen en minúsculas ("true" / "false").


def bool_text(value):
    # Convierte True/False en "true"/"false" para imprimirlos
    return str(value).lower()


# Problem 1: Shopping list basics
# Description:
#   Lee una lista de compras escrita como texto separado por comas, la convierte
#   en lista con split(","), limpia cada elemento con strip() y descarta los
#   pedazos vacíos. Luego agrega un elemento nuevo con append() y revisa si el
#   elemento buscado está en la lista.
#   Decisión: una lista inicial vacía se rechaza con un error.
#   Decisión: la búsqueda NO distingue mayúsculas de minúsculas; los elementos y el
#   texto buscado se comparan en minúsculas (lower()), pero la lista conserva el
#   texto original que escribió el usuario.
#   Found item: true significa que el elemento buscado está en la lista (incluyendo
#   el elemento nuevo); false significa que no está.
# Inputs:
#   initial_items_text (string, por ejemplo "apple,banana,orange")
#   new_item (string)
#   search_item (string)
# Outputs:
#   "Items list: <list>"
#   "Total items: <n>"
#   "Found item: true/false"
# Validations:
#   - initial_items_text no vacío después de strip() y con al menos un elemento
#     después de quitar los pedazos vacíos.
#   - new_item y search_item no vacíos después de strip().
#   - Si no se cumple, "Error: invalid input".
# Test cases:
#   1) Normal: "apple,banana,orange", "grape", "banana"
#      -> Items list: ['apple', 'banana', 'orange', 'grape'] |
#         Total items: 4 | Found item: true
#   2) Border: " apple , ,Banana ", "kiwi", "BANANA"
#      (espacios de más, un pedazo vacío y mayúsculas diferentes)
#      -> Items list: ['apple', 'Banana', 'kiwi'] | Total items: 3 |
#         Found item: true

ITEM_SEPARATOR = ","


def problem_1():
    print("Problem 1: Shopping list basics")
    initial_items_text = input("Enter items separated by commas: ")
    new_item = input("Enter a new item: ").strip()
    search_item = input("Enter an item to search: ").strip()

    if initial_items_text.strip() == "" or new_item == "" or search_item == "":
        print("Error: invalid input")
        return

    items_list = []
    for piece in initial_items_text.split(ITEM_SEPARATOR):
        clean_piece = piece.strip()
        if clean_piece != "":
            items_list.append(clean_piece)

    if len(items_list) == 0:
        print("Error: invalid input")
        return

    items_list.append(new_item)

    # Se arma una copia en minúsculas solo para la comparación
    lower_items = []
    for item in items_list:
        lower_items.append(item.lower())
    is_in_list = search_item.lower() in lower_items

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {bool_text(is_in_list)}")


# Problem 2: Points with tuples
# Description:
#   Lee las coordenadas de dos puntos y guarda cada uno en una tupla
#   (inmutable): point_a = (x1, y1), point_b = (x2, y2).
#   Calcula la distancia entre ellos:
#   distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#   y el punto medio: ((x1 + x2) / 2, (y1 + y2) / 2).
# Inputs:
#   x1, y1, x2, y2 (float)
# Outputs:
#   "Point A: (x1, y1)"
#   "Point B: (x2, y2)"
#   "Distance: <value>" (redondeado a 2 decimales)
#   "Midpoint: (mx, my)"
# Validations:
#   - Los cuatro valores deben poder convertirse a float con try/except ValueError;
#     si no, "Error: invalid input".
# Test cases:
#   1) Normal: 0, 0, 3, 4 -> Point A: (0.0, 0.0) | Point B: (3.0, 4.0) |
#      Distance: 5.0 | Midpoint: (1.5, 2.0)
#   2) Border: 2, 2, 2, 2 (el mismo punto) -> Point A: (2.0, 2.0) |
#      Point B: (2.0, 2.0) | Distance: 0.0 | Midpoint: (2.0, 2.0)


def problem_2():
    print("Problem 2: Points with tuples")
    x1_text = input("Enter x1: ")
    y1_text = input("Enter y1: ")
    x2_text = input("Enter x2: ")
    y2_text = input("Enter y2: ")

    try:
        x1 = float(x1_text)
        y1 = float(y1_text)
        x2 = float(x2_text)
        y2 = float(y2_text)
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5
    midpoint = ((point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2)

    print(f"Point A: ({point_a[0]}, {point_a[1]})")
    print(f"Point B: ({point_b[0]}, {point_b[1]})")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: ({round(midpoint[0], 2)}, {round(midpoint[1], 2)})")


# Problem 3: Product catalog with a dictionary
# Description:
#   Usa un diccionario product_prices (nombre del producto -> precio unitario) para
#   encontrar el precio de un producto y calcular el total según la cantidad.
#   El nombre del producto se normaliza con strip().lower() porque las
#   claves están en minúsculas.
#   Catálogo: apple 10.0, banana 5.5, milk 25.0, bread 30.0
# Inputs:
#   product_name (string), quantity (int)
# Outputs:
#   "Unit price: <value>"
#   "Quantity: <n>"
#   "Total: <value>" (redondeado a 2 decimales)
# Validations:
#   - product_name no vacío después de strip().
#   - quantity debe poder convertirse a int y ser > 0.
#   - Si no se cumple, "Error: invalid input".
#   - Si el producto no es una clave del diccionario: "Error: product not found".
# Test cases:
#   1) Normal: "pepsi", 2 -> Unit price: 25.0 | Quantity: 2 | Total: 50.0
#   2) Border: "  CEBOLLA  ", 1 (espacios, mayúsculas y cantidad mínima)
#      -> Unit price: 30.0 | Quantity: 1 | Total: 30.0

MIN_QUANTITY = 1


def problem_3():
    print("Problem 3: Product catalog")
    product_prices = {"chetos": 10.0, "doritos": 5.5, "pepsi": 25.0, "cebolla": 30.0}

    product_name = input("Enter product name: ").strip().lower()
    quantity_text = input("Enter quantity: ")

    if product_name == "":
        print("Error: invalid input")
        return

    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Error: invalid input")
        return

    if quantity < MIN_QUANTITY:
        print("Error: invalid input")
        return

    if product_name not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[product_name]
    total = unit_price * quantity

    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {round(total, 2)}")


# Problem 4: Student grades (dictionary of lists)
# Description:
#   Usa un diccionario donde cada clave es el nombre de un alumno y cada valor
#   es una lista de calificaciones. Calcula el promedio del alumno elegido
#   y decide si aprobó.
#   Decisión: el nombre se normaliza con strip().title(), así que "alice",
#   "ALICE" y " Alice " coinciden con la clave "Alice".
#   Passed: true significa average >= PASSING_GRADE (70.0); si no, false.
# Inputs:
#   student_name (string)
# Outputs:
#   "Grades: <list>"
#   "Average: <value>" (redondeado a 2 decimales)
#   "Passed: true/false"
# Validations:
#   - student_name no vacío después de strip(); si no, "Error: invalid input".
#   - Si el nombre no es una clave: "Error: student not found".
#   - Si la lista de calificaciones
#   está vacía: "Error: no grades available"
#     (evita dividir entre cero).
# Test cases:
#   1) Normal: "Antonio" -> Grades: [90.0, 85.0, 78.0] | Average: 84.33 |
#      Passed: true
#   2) Border: "Charly" (promedio de exactamente 70.0) -> Grades: [70.0, 70.0, 70.0] |
#      Average: 70.0 | Passed: true

PASSING_GRADE = 70.0


def problem_4():
    print("Problem 4: Student grades")
    student_grades = {
        "Antonio": [90.0, 85.0, 78.0],
        "Cristian": [60.0, 65.0, 70.0],
        "Charly": [70.0, 70.0, 70.0],
        "Andrea": [],
    }

    student_name = input("Enter student name: ").strip().title()

    if student_name == "":
        print("Error: invalid input")
        return

    if student_name not in student_grades:
        print("Error: student not found")
        return

    grades = student_grades[student_name]
    if len(grades) == 0:
        print("Error: no grades available")
        return

    average = round(sum(grades) / len(grades), 2)
    is_passed = average >= PASSING_GRADE

    print(f"Grades: {grades}")
    print(f"Average: {average}")
    print(f"Passed: {bool_text(is_passed)}")


# Problem 5: Word frequency
# Description:
#   Lee una oración, la pasa a minúsculas, quita la puntuación sencilla
#   y cuenta cuántas veces aparece cada palabra usando un
#   diccionario (palabra -> conteo). Luego encuentra la palabra más común.
#   Decisión: los caracteres . , ; : ! ? se quitan con replace();
#   los demás símbolos se quedan como parte de la palabra.
#   Decisión: si hay empate, la palabra más común es la primera que se encontró.
# Inputs:
#   sentence (string)
# Outputs:
#   "Words list: <list>"
#   "Frequencies: <dict>"
#   "Most common word: <word>"
# Validations:
#   - sentence no vacía después de strip().
#   - Al menos una palabra después de quitar la puntuación y usar split().
#   - Si no se cumple, "Error: invalid input".
# Test cases:
#   1) Normal: "The cat and the dog and the bird."
#      -> Words list: ['the', 'cat', 'and', 'the', 'dog', 'and', 'the', 'bird'] |
#         Frequencies: {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1} |
#         Most common word: the
#   2) Border: "Hi!" (una sola palabra)
#      -> Words list: ['hi'] | Frequencies: {'hi': 1} | Most common word: hi

PUNCTUATION_MARKS = [".", ",", ";", ":", "!", "?"]


def problem_5():
    print("Problem 5: Word frequency")
    sentence = input("Enter a sentence: ")
    clean_sentence = sentence.strip().lower()

    if clean_sentence == "":
        print("Error: invalid input")
        return

    for mark in PUNCTUATION_MARKS:
        clean_sentence = clean_sentence.replace(mark, "")

    words_list = clean_sentence.split()
    if len(words_list) == 0:
        print("Error: invalid input")
        return

    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common_word = words_list[0]
    for word in freq_dict:
        if freq_dict[word] > freq_dict[most_common_word]:
            most_common_word = word

    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


# Problem 6: Contact book (add, search, delete)
# Description:
#   Usa un diccionario contacts (nombre -> teléfono) como una pequeña agenda.
#   El usuario elige una acción: ADD guarda un contacto nuevo (o actualiza el
#   teléfono si ya existe), SEARCH muestra el teléfono con get() y
#   DELETE borra el contacto con pop().
#   La acción se normaliza con strip().upper() y el nombre con
#   strip().title(). El teléfono solo se pide cuando la acción es ADD.
#   Contactos iniciales: Alice 1234567890, Bob 5551234567, Carlos 8341234567
# Inputs:
#   action_text ("ADD", "SEARCH" o "DELETE"), name (string),
#   phone (string, solo para ADD)
# Outputs:
#   ADD: "Contact saved: <name>, <phone>"
#   SEARCH: "Phone: <phone>" o "Error: contact not found"
#   DELETE: "Contact deleted: <name>" o "Error: contact not found"
# Validations:
#   - action_text debe ser ADD, SEARCH o DELETE.
#   - name no vacío después de strip(); phone no vacío para ADD.
#   - Si no se cumple, "Error: invalid input".
# Test cases:
#   1) Normal: "ADD", " diana ", "8112345678"
#      -> Contact saved: Diana, 8112345678
#   2) Border: "  search ", "CHARLY" (espacios y mayúsculas diferentes)
#      -> Phone: 1234567890

ADD_ACTION = "ADD"
SEARCH_ACTION = "SEARCH"
DELETE_ACTION = "DELETE"
VALID_ACTIONS = (ADD_ACTION, SEARCH_ACTION, DELETE_ACTION)


def problem_6():
    print("Problem 6: Contact book")
    contacts = {"Charly": "1234567890", "Cristian": "5551234567", "Carlos": "8341234567"}

    action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
    name = input("Enter contact name: ").strip().title()
    phone = ""
    if action_text == ADD_ACTION:
        phone = input("Enter phone number: ").strip()

    if action_text not in VALID_ACTIONS or name == "":
        print("Error: invalid input")
        return

    if action_text == ADD_ACTION:
        if phone == "":
            print("Error: invalid input")
            return
        contacts[name] = phone
        print(f"Contact saved: {name}, {contacts[name]}")
    elif action_text == SEARCH_ACTION:
        found_phone = contacts.get(name)
        if found_phone is None:
            print("Error: contact not found")
        else:
            print(f"Phone: {found_phone}")
    elif action_text == DELETE_ACTION:
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")


# PROGRAMA PRINCIPAL

def main():
    problem_1()
    print()
    problem_2()
    print()
    problem_3()
    print()
    problem_4()
    print()
    problem_5()
    print()
    problem_6()


if __name__ == "__main__":
    main()


# CONCLUSIONES
# Las listas son la colección más flexible: son ideales cuando los elementos se
# agregan o se quitan seguido, como en una lista de compras.
# Las tuplas son mejores para datos fijos que no deben cambiar, como las
# coordenadas de un punto.
# Los diccionarios permiten buscar rápido por clave, lo cual es perfecto para catálogos,
# calificaciones y agendas de contactos.
# Patrones como un diccionario de listas (alumno -> calificaciones) o un diccionario de conteos
# (palabra -> frecuencia) resuelven muchos problemas reales con poco código.
# Normalizar las claves con strip(), lower() o title() y validar los
# datos vacíos evita errores como "not found" o la división entre cero.


# REFERENCIAS
# 1) Tutorial oficial de Python - Data Structures (listas, tuplas, diccionarios).
#    https://docs.python.org/3/tutorial/datastructures.html
# 2) Documentación oficial de Python - Built-in Types: Sequence Types (list, tuple, range).
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 3) Documentación oficial de Python - Built-in Types: Mapping Types (dict).
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# 4) PEP 8 - Style Guide for Python Code (guía de estilo de Python).
#    https://peps.python.org/pep-0008/
# 5) W3Schools - Python Lists.
#    https://www.w3schools.com/python/python_lists.asp
# 6) W3Schools - Python Dictionaries.
#    https://www.w3schools.com/python/python_dictionaries.asp
# 7) Real Python - Lists and Tuples in Python.
#    https://realpython.com/python-lists-tuples/
# 8) Real Python - Dictionaries in Python.
#    https://realpython.com/python-dicts/
