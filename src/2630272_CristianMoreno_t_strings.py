# PORTADA 

# Tarea: Cadenas de texto (strings) en Python (t_strings)
# Nombre: Cristian Eduardo Moreno Hernandez
# Matrícula: 2630272
# Grupo: TSU-75004

# RESUMEN EJECUTIVO
# Un string en Python es un tipo de dato (str) que guarda una secuencia de caracteres.
# Los strings son inmutables: una vez creados no se pueden cambiar; cada operación
# como upper() o replace() regresa un string nuevo.
# Las operaciones básicas incluyen la concatenación (+), la repetición (*), obtener la
# longitud con len(), extraer subcadenas con indexación y slicing,
# buscar patrones con find() o "in", y reemplazar texto con replace().
# Validar y normalizar la entrada del usuario (correos, nombres, contraseñas) es
# importante porque la gente escribe espacios de más o mezcla mayúsculas, y los datos
# malos causan errores después. Este documento cubre seis problemas, cada uno con su
# descripción, diseño de entradas y salidas, validaciones, métodos de string usados
# y dos casos de prueba (normal y borde), junto con el código.

# PRINCIPIOS Y BUENAS PRÁCTICAS
# - Los strings son inmutables: cualquier cambio crea un string nuevo.
# - Normalizar la entrada con strip() y lower() antes de compararla.
# - Evitar "números mágicos" en los índices; usar constantes con nombre y documentar
#   qué extrae cada slice.
# - Usar los métodos de string que ya trae Python en lugar de reescribir lógica básica.
# - Diseñar validaciones claras: primero revisar que el texto no esté vacío,
#   luego revisar su formato.
# - Escribir código legible: nombres de variables claros y mensajes de error
#   fáciles de entender.


# Problem 1: Full name formatter
# Description:
#   Lee un nombre completo, quita los espacios de más, pone en mayúscula la
#   primera letra de cada palabra con title() y arma las iniciales (por ejemplo "C.E.M.H.").
# Inputs:
#   full_name (string)
# Outputs:
#   "Formatted name: <name>"
#   "Initials: <initials>"
# Validations:
#   - El nombre no debe quedar vacío después de strip().
#   - El nombre debe tener al menos MIN_WORDS palabras (nombre y apellido).
# Test cases:
#   1) Normal: "cristian eduardo moreno hernandez"
#      -> Formatted name: Cristian Eduardo Moreno Hernandez | Initials: C.E.M.H.
#   2) Border: "   ANA    lopez  " (espacios de más, mayúsculas y minúsculas mezcladas)
#      -> Formatted name: Ana Lopez | Initials: A.L.
MIN_WORDS = 2


def problem_1():
    print("--- Problem 1: Full name formatter ---")
    full_name = input("Enter your full name: ")
    clean_name = full_name.strip()

    if clean_name == "":
        print("Error: invalid input (empty name)")
        return

    # split() sin argumentos también elimina los espacios repetidos de en medio
    words = clean_name.split()
    if len(words) < MIN_WORDS:
        print("Error: invalid input (at least two words required)")
        return

    formatted_name = " ".join(words).title()
    initials = ""
    for word in words:
        # word[0] es la primera letra de cada palabra
        initials = initials + word[0].upper() + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# Problem 2: Simple email validator (structure + domain)
# Description:
#   Lee un correo y revisa una estructura sencilla. El correo es válido si:
#   - tiene exactamente un '@' (se revisa con count()),
#   - después del '@' hay al menos un '.',
#   - no tiene espacios en blanco adentro.
#   Si es válido, también muestra el dominio (la parte después del '@').
# Inputs:
#   email_text (string)
# Outputs:
#   "Valid email: true" o "Valid email: false"
#   Si es válido: "Domain: <domain_part>"
# Validations:
#   - No vacío después de strip().
#   - Contar los '@' con count() (debe haber exactamente 1).
#   - Verificar que no haya " " en el correo. strip() solo quita los
#     espacios de afuera, así que un correo con espacios adentro sigue siendo inválido.
# Test cases:
#   1) Normal: "2630272@upv.edu.mx"
#      -> Valid email: true | Domain: upv.edu.mx
#   2) Border: "  cristian.moreno@upv.edu.mx  " (solo espacios afuera, strip() los quita)
#      -> Valid email: true | Domain: upv.edu.mx
AT_SYMBOL = "@"
DOT_SYMBOL = "."
REQUIRED_AT_COUNT = 1


def problem_2():
    print("--- Problem 2: Email validator ---")
    email_text = input("Enter your email: ")
    clean_email = email_text.strip()

    if clean_email == "":
        print("Error: invalid input (empty email)")
        return

    is_valid = True
    domain_part = ""

    if " " in clean_email:
        is_valid = False
    elif clean_email.count(AT_SYMBOL) != REQUIRED_AT_COUNT:
        is_valid = False
    else:
        at_position = clean_email.find(AT_SYMBOL)
        domain_part = clean_email[at_position + 1:]  # texto después del '@'
        if DOT_SYMBOL not in domain_part:
            is_valid = False

    if is_valid:
        print("Valid email: true")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")


# Problem 3: Palindrome checker (ignoring spaces and case)
# Description:
#   Lee una palabra o frase y revisa si se lee igual al derecho y
#   al revés. El texto se normaliza con lower() y
#   replace(" ", ""), y luego se compara con su reverso text[::-1] usando ==.
#   Ejemplos: "Anita lava la tina" -> true, "Hola mundo" -> false.
# Inputs:
#   phrase_text (string)
# Outputs:
#   "Normalized text: <text>"
#   "Is palindrome: true" o "Is palindrome: false"
# Validations:
#   - No vacío después de strip().
#   - Al menos MIN_PALINDROME_LENGTH (3) caracteres después de quitar los espacios.
# Test cases:
#   1) Normal: "Anita lava la tina"
#      -> Normalized text: anitalavalatina | Is palindrome: true
#   2) Border: "ana" (exactamente 3 caracteres, el mínimo)
#      -> Normalized text: ana | Is palindrome: true
MIN_PALINDROME_LENGTH = 3


def problem_3():
    print("--- Problem 3: Palindrome checker ---")
    phrase_text = input("Enter a word or phrase: ")
    clean_phrase = phrase_text.strip()

    if clean_phrase == "":
        print("Error: invalid input (empty text)")
        return

    normalized_text = clean_phrase.lower().replace(" ", "")

    if len(normalized_text) < MIN_PALINDROME_LENGTH:
        print(f"Error: invalid input (at least {MIN_PALINDROME_LENGTH} characters required)")
        return

    reversed_text = normalized_text[::-1]  # todo el string con paso -1 (al revés)
    print(f"Normalized text: {normalized_text}")
    if normalized_text == reversed_text:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# Problem 4: Sentence word statistics
# Description:
#   Lee una oración, la limpia con strip(), la divide en palabras con
#   split() y muestra: el número de palabras, la primera palabra, la última
#   palabra, la palabra más corta y la más larga. La más corta y la más
#   larga se encuentran recorriendo la lista de palabras con un ciclo
#   (si hay empate, se queda la primera que se encontró).
# Inputs:
#   sentence_text (string)
# Outputs:
#   "Word count: <n>"
#   "First word: <word>"
#   "Last word: <word>"
#   "Shortest word: <word>"
#   "Longest word: <word>"
# Validations:
#   - No vacía después de strip().
#   - Al menos una palabra después de split().
# Test cases:
#   1) Normal: "Python is a great language"
#      -> Word count: 5 | First word: Python | Last word: language |
#         Shortest word: a | Longest word: language
#   2) Border: "   hello   " (una sola palabra, con espacios de más)
#      -> Word count: 1 | First word: hello | Last word: hello |
#         Shortest word: hello | Longest word: hello
MIN_WORD_COUNT = 1
FIRST_INDEX = 0
LAST_INDEX = -1


def problem_4():
    print("--- Problem 4: Sentence word statistics ---")
    sentence_text = input("Enter a sentence: ")
    clean_sentence = sentence_text.strip()

    if clean_sentence == "":
        print("Error: invalid input (empty sentence)")
        return

    words = clean_sentence.split()
    word_count = len(words)
    if word_count < MIN_WORD_COUNT:
        print("Error: invalid input (no words found)")
        return

    first_word = words[FIRST_INDEX]
    last_word = words[LAST_INDEX]

    shortest_word = words[FIRST_INDEX]
    longest_word = words[FIRST_INDEX]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# Problem 5: Password strength classifier
# Description:
#   Clasifica una contraseña como "weak", "medium" o "strong".
#   Reglas usadas en esta solución:
#   - weak:   longitud < MIN_LENGTH (8), O solo tiene un tipo de
#             carácter (por ejemplo solo minúsculas o solo dígitos).
#   - medium: longitud >= 8 y tiene al menos dos tipos de caracteres
#             (mayúsculas, minúsculas, dígitos, símbolos) pero no los cuatro.
#   - strong: longitud >= 8 y tiene al menos una letra mayúscula,
#             una letra minúscula, un dígito y un símbolo
#             (carácter no alfanumérico, como !, @, #).
# Inputs:
#   password_input (string)
# Outputs:
#   "Password strength: weak" / "medium" / "strong"
# Validations:
#   - La contraseña no debe quedar vacía después de strip().
#   - La longitud se revisa con len().
# Test cases:
#   1) Normal: "Hola2026!"
#      -> Password strength: strong
#   2) Border: "abcdefg1" (exactamente 8 caracteres, minúsculas + dígito)
#      -> Password strength: medium
#   Extra: "abc" -> Password strength: weak
MIN_LENGTH = 8
MIN_TYPES_MEDIUM = 2


def problem_5():
    print("--- Problem 5: Password strength classifier ---")
    password_input = input("Enter a password: ")
    clean_password = password_input.strip()

    if clean_password == "":
        print("Error: invalid input (empty password)")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in clean_password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    # True cuenta como 1 y False como 0
    character_types = has_upper + has_lower + has_digit + has_symbol

    if len(clean_password) < MIN_LENGTH or character_types < MIN_TYPES_MEDIUM:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Length: {len(clean_password)}")
    print(f"Password strength: {strength}")


# Problem 6: Product label formatter (fixed-width text)
# Description:
#   Arma una etiqueta de una sola línea "Product: <NAME> | Price: $<PRICE>" que
#   debe tener exactamente LABEL_WIDTH (30) caracteres: si es más corta se
#   rellena con espacios al final, si es más larga se recorta con
#   el slice label[:30]. La etiqueta se muestra entre comillas para que
#   se vean los espacios.
# Inputs:
#   product_name (string)
#   price_value (string, se convierte a número positivo con float())
# Outputs:
#   'Label: "<exactly 30 characters>"'
#   "Length: 30"
# Validations:
#   - product_name no vacío después de strip().
#   - price_value debe poder convertirse a un número mayor que 0.
# Test cases:
#   1) Normal: product_name="Pen", price_value="12.5"
#      -> Label: "Product: Pen | Price: $12.50  " | Length: 30
#   2) Border: product_name="Wireless Keyboard", price_value="899"
#      -> Label: "Product: Wireless Keyboard | P" | Length: 30
LABEL_WIDTH = 30


def problem_6():
    print("--- Problem 6: Product label formatter ---")
    product_name = input("Enter the product name: ")
    price_value = input("Enter the price: ")
    clean_name = product_name.strip()
    clean_price = price_value.strip()

    if clean_name == "":
        print("Error: invalid input (empty product name)")
        return

    # intentar convertir el texto del precio a número
    try:
        price_number = float(clean_price)
    except ValueError:
        print("Error: invalid input (price must be a positive number)")
        return

    if price_number <= 0:
        print("Error: invalid input (price must be a positive number)")
        return

    label = f"Product: {clean_name} | Price: ${price_number:.2f}"

    if len(label) < LABEL_WIDTH:
        # rellenar con espacios al final
        label = label + " " * (LABEL_WIDTH - len(label))
    else:
        # dejar solo los primeros LABEL_WIDTH caracteres
        label = label[:LABEL_WIDTH]

    print(f'Label: "{label}"')
    print(f"Length: {len(label)}")


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
# El manejo de strings es esencial en la entrada y salida de datos, porque casi todo
# lo que escribe el usuario llega como texto y se tiene que mostrar como texto.
# strip() quita espacios accidentales, lower() hace que las comparaciones sean justas,
# split() convierte una oración en palabras y join() vuelve a armar el texto.
# Normalizar el texto antes de compararlo evita resultados falsos; por ejemplo,
# "Anita lava la tina" solo es palíndromo después de usar lower() y replace().
# Revisar primero que la entrada no esté vacía y luego su formato evita
# errores y datos basura en el programa.
# Aprendí que los strings son inmutables, así que cada método regresa un string
# nuevo, y que los slices como text[:30] o text[::-1] extraen o
# invierten partes de un string sin usar ciclos.

# REFERENCIAS
# 1) Documentación oficial de Python - Built-in Types: Text Sequence Type - str.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Tutorial oficial de Python - An Informal Introduction to Python: Text.
#    https://docs.python.org/3/tutorial/introduction.html#text
# 3) PEP 8 - Style Guide for Python Code (guía de estilo de Python).
#    https://peps.python.org/pep-0008/
# 4) W3Schools - Python Strings.
#    https://www.w3schools.com/python/python_strings.asp
# 5) Real Python - Strings and Character Data in Python.
#    https://realpython.com/python-strings/
# 6) Documentación oficial de Python - Input and Output (f-strings / formatted literals).
#    https://docs.python.org/3/tutorial/inputoutput.html
