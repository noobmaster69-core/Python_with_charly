# PORTADA

# Tarea: Tipos de datos numéricos y booleanos en Python
# Nombre: Cristian Eduardo Moreno Hernandez
# Matrícula: 2630272
# Grupo: TSU-75004

# RESUMEN EJECUTIVO
# Python tiene dos tipos numéricos principales: int guarda números enteros (5, -3)
# y float guarda números con decimales (36.6, 1.5).
# Si se mezclan en una operación el resultado es float, y "/" siempre regresa un float.
# Un bool es un valor que solo puede ser True o False; normalmente es el
# resultado de una comparación como temp_c >= 30.0 o score >= 650.
# Antes de calcular hay que validar la entrada: convertir el texto con
# int() o float(), revisar que los rangos sean válidos (sin horas negativas, sin
# temperaturas debajo del cero absoluto) y evitar la división entre cero.
# Este documento cubre seis problemas con su descripción, entradas,
# salidas, validaciones, dos casos de prueba cada uno (normal y borde) y el código en Python.

# PRINCIPIOS Y BUENAS PRÁCTICAS
# 1) Usar int para conteos y valores enteros, y float para medidas y dinero.
# 2) Validar y convertir la entrada con try/except ValueError antes de usarla.
# 3) Revisar los rangos y nunca dividir entre cero (income > 0, height > 0).
# 4) Usar constantes con nombre (UPPER_SNAKE_CASE) en lugar de "números mágicos".
# 5) Guardar el resultado de las comparaciones en variables booleanas claras
#    (has_overtime, discount_eligible) y redondear el dinero a 2 decimales.
# Nota: los booleanos se imprimen en minúsculas ("true" / "false").


def bool_text(value):
    # Convierte True/False en "true"/"false" para imprimirlos
    return str(value).lower()


# Problem 1: Temperature converter and range flag
# Description:
#   Lee una temperatura en grados Celsius y la convierte a Fahrenheit y
#   Kelvin. También activa una bandera booleana de temperatura alta.
#   Fórmulas: temp_f = temp_c * 9 / 5 + 32, temp_k = temp_c + 273.15
#   High temperature: true significa temp_c >= HIGH_TEMP_THRESHOLD (30.0 C),
#   false significa temp_c < 30.0 C.
# Inputs:
#   temp_c (float, grados Celsius)
# Outputs:
#   "Fahrenheit: <value>"
#   "Kelvin: <value>"
#   "High temperature: true/false"
# Validations:
#   - temp_c debe poder convertirse a float; si no, "Error: invalid input".
#   - temp_k no puede ser menor que 0.0 (cero absoluto); si lo es,
#     "Error: invalid input".
# Test cases:
#   1) Normal: 25 -> Fahrenheit: 77.0 | Kelvin: 298.15 | High temperature: false
#   2) Border: 30.0 -> Fahrenheit: 86.0 | Kelvin: 303.15 | High temperature: true
#      (justo en el límite cuenta como temperatura alta)
HIGH_TEMP_THRESHOLD = 30.0
KELVIN_OFFSET = 273.15
ABSOLUTE_ZERO_K = 0.0


def problem_1():
    print("--- Problem 1: Temperature converter ---")
    temp_c_text = input("Enter temperature in Celsius: ")

    try:
        temp_c = float(temp_c_text)
    except ValueError:
        print("Error: invalid input")
        return

    temp_k = temp_c + KELVIN_OFFSET
    if temp_k < ABSOLUTE_ZERO_K:
        print("Error: invalid input")
        return

    temp_f = temp_c * 9 / 5 + 32
    is_high_temperature = temp_c >= HIGH_TEMP_THRESHOLD

    print(f"Fahrenheit: {round(temp_f, 2)}")
    print(f"Kelvin: {round(temp_k, 2)}")
    print(f"High temperature: {bool_text(is_high_temperature)}")


# Problem 2: Work hours and overtime
# Description:
#   Calcula el pago semanal de un trabajador. Hasta REGULAR_HOURS (40)
#   horas se pagan a hourly_rate; las horas arriba de 40 se pagan al 150%
#   (hourly_rate * OVERTIME_MULTIPLIER). Usa min() y max():
#   regular_hours = min(hours_worked, 40)
#   overtime_hours = max(hours_worked - 40, 0)
#   Has overtime: true significa hours_worked > 40, false significa <= 40.
# Inputs:
#   hours_worked (float), hourly_rate (float)
# Outputs:
#   "Regular pay: <value>"
#   "Overtime pay: <value>"
#   "Total pay: <value>"
#   "Has overtime: true/false"
# Validations:
#   - Ambos valores deben poder convertirse a float.
#   - hours_worked >= 0 y hourly_rate > 0; si no, "Error: invalid input".
# Test cases:
#   1) Normal: hours=45, rate=100 -> Regular pay: 4000.0 |
#      Overtime pay: 750.0 | Total pay: 4750.0 | Has overtime: true
#   2) Border: hours=40, rate=100 -> Regular pay: 4000.0 |
#      Overtime pay: 0.0 | Total pay: 4000.0 | Has overtime: false
REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5
MIN_HOURS = 0.0
MIN_RATE = 0.0


def problem_2():
    print("--- Problem 2: Work hours and overtime ---")
    hours_text = input("Enter hours worked: ")
    rate_text = input("Enter hourly rate: ")

    try:
        hours_worked = float(hours_text)
        hourly_rate = float(rate_text)
    except ValueError:
        print("Error: invalid input")
        return

    if hours_worked < MIN_HOURS or hourly_rate <= MIN_RATE:
        print("Error: invalid input")
        return

    regular_hours = min(hours_worked, REGULAR_HOURS)
    overtime_hours = max(hours_worked - REGULAR_HOURS, 0)

    regular_pay = round(regular_hours * hourly_rate, 2)
    overtime_pay = round(overtime_hours * hourly_rate * OVERTIME_MULTIPLIER, 2)
    total_pay = round(regular_pay + overtime_pay, 2)
    has_overtime = hours_worked > REGULAR_HOURS

    print(f"Regular pay: {regular_pay}")
    print(f"Overtime pay: {overtime_pay}")
    print(f"Total pay: {total_pay}")
    print(f"Has overtime: {bool_text(has_overtime)}")


# Problem 3: Discount eligibility with booleans
# Description:
#   Lee el total de la compra y dos respuestas YES/NO (estudiante y
#   adulto mayor). Los textos se normalizan con strip().upper() y se
#   convierten en booleanos comparándolos con "YES".
#   discount_eligible = is_student or is_senior or
#                       (purchase_total >= MIN_PURCHASE_FOR_DISCOUNT)
#   Si aplica, se hace un descuento de DISCOUNT_RATE (10%):
#   final_total = purchase_total * 0.9; si no, final_total = purchase_total.
#   Discount eligible: true significa que se aplicó el descuento,
#   false significa que el cliente paga el total completo.
# Inputs:
#   purchase_total (float), is_student_text ("YES"/"NO"),
#   is_senior_text ("YES"/"NO")
# Outputs:
#   "Discount eligible: true/false"
#   "Final total: <value>" (redondeado a 2 decimales)
# Validations:
#   - purchase_total debe poder convertirse a float y ser >= 0.0.
#   - Ambos textos deben ser "YES" o "NO" después de strip().upper();
#     si no, "Error: invalid input".
# Test cases:
#   1) Normal: purchase=500, student="yes", senior="no"
#      -> Discount eligible: true | Final total: 450.0
#   2) Border: purchase=1000, student=" no ", senior="NO"
#      (justo la compra mínima, sin ser estudiante ni adulto mayor)
#      -> Discount eligible: true | Final total: 900.0
DISCOUNT_RATE = 0.10
MIN_PURCHASE_FOR_DISCOUNT = 1000.0
MIN_PURCHASE = 0.0
YES_TEXT = "YES"
NO_TEXT = "NO"


def problem_3():
    print("--- Problem 3: Discount eligibility ---")
    purchase_text = input("Enter purchase total: ")
    is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

    try:
        purchase_total = float(purchase_text)
    except ValueError:
        print("Error: invalid input")
        return

    if purchase_total < MIN_PURCHASE:
        print("Error: invalid input")
        return
    if is_student_text != YES_TEXT and is_student_text != NO_TEXT:
        print("Error: invalid input")
        return
    if is_senior_text != YES_TEXT and is_senior_text != NO_TEXT:
        print("Error: invalid input")
        return

    is_student = is_student_text == YES_TEXT
    is_senior = is_senior_text == YES_TEXT
    discount_eligible = is_student or is_senior or (purchase_total >= MIN_PURCHASE_FOR_DISCOUNT)

    if discount_eligible:
        final_total = purchase_total * (1 - DISCOUNT_RATE)
    else:
        final_total = purchase_total

    print(f"Discount eligible: {bool_text(discount_eligible)}")
    print(f"Final total: {round(final_total, 2)}")


# Problem 4: Basic statistics of three integers
# Description:
#   Lee exactamente tres números enteros (uno por pregunta) y muestra la suma,
#   el promedio, el máximo, el mínimo y si los tres son pares.
#   sum_value = n1 + n2 + n3, average_value = sum_value / 3
#   All even: true significa que n1, n2 y n3 son divisibles entre 2
#   (number % 2 == 0); false significa que al menos uno es impar.
# Inputs:
#   n1, n2, n3 (int, se permiten negativos)
# Outputs:
#   "Sum: <value>"
#   "Average: <value>" (redondeado a 2 decimales)
#   "Max: <value>"
#   "Min: <value>"
#   "All even: true/false"
# Validations:
#   - Cada valor debe poder convertirse a int; si no, "Error: invalid input".
# Test cases:
#   1) Normal: n1=4, n2=7, n3=10 -> Sum: 21 | Average: 7.0 | Max: 10 |
#      Min: 4 | All even: false
#   2) Border: n1=-2, n2=0, n3=8 (negativo y cero) -> Sum: 6 |
#      Average: 2.0 | Max: 8 | Min: -2 | All even: true
NUMBER_COUNT = 3


def problem_4():
    print("--- Problem 4: Basic statistics of three integers ---")
    n1_text = input("Enter integer 1: ")
    n2_text = input("Enter integer 2: ")
    n3_text = input("Enter integer 3: ")

    try:
        n1 = int(n1_text)
        n2 = int(n2_text)
        n3 = int(n3_text)
    except ValueError:
        print("Error: invalid input")
        return

    sum_value = n1 + n2 + n3
    average_value = sum_value / NUMBER_COUNT
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {bool_text(all_even)}")


# Problem 5: Loan eligibility
# Description:
#   Decide si una persona puede obtener un préstamo. debt_ratio = monthly_debt /
#   monthly_income. Eligible: true cuando se cumplen TODAS estas reglas:
#   - monthly_income >= MIN_INCOME (8000.0)
#   - debt_ratio <= MAX_DEBT_RATIO (0.4)
#   - credit_score >= MIN_CREDIT_SCORE (650)
#   Eligible: false cuando falla al menos una regla.
# Inputs:
#   monthly_income (float), monthly_debt (float), credit_score (int)
# Outputs:
#   "Debt ratio: <value>" (redondeado a 2 decimales)
#   "Eligible: true/false"
# Validations:
#   - Los valores deben poder convertirse (float, float, int); si no, error.
#   - monthly_income > 0.0 (evita dividir entre cero), monthly_debt >= 0.0,
#     credit_score >= 0; si no, "Error: invalid input".
# Test cases:
#   1) Normal: income=20000, debt=5000, score=700
#      -> Debt ratio: 0.25 | Eligible: true
#   2) Border: income=8000, debt=3200, score=650 (todo justo en los límites)
#      -> Debt ratio: 0.4 | Eligible: true
MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650


def problem_5():
    print("--- Problem 5: Loan eligibility ---")
    income_text = input("Enter monthly income: ")
    debt_text = input("Enter monthly debt: ")
    score_text = input("Enter credit score: ")

    try:
        monthly_income = float(income_text)
        monthly_debt = float(debt_text)
        credit_score = int(score_text)
    except ValueError:
        print("Error: invalid input")
        return

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return

    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_INCOME
                and debt_ratio <= MAX_DEBT_RATIO
                and credit_score >= MIN_CREDIT_SCORE)

    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {bool_text(eligible)}")


# Problem 6: BMI calculator
# Description:
#   Calcula el Índice de Masa Corporal: bmi = weight_kg / (height_m * height_m)
#   y muestra tres booleanos usando comparaciones encadenadas:
#   - Underweight: true cuando bmi < UNDERWEIGHT_LIMIT (18.5)
#   - Normal: true cuando 18.5 <= bmi < OVERWEIGHT_LIMIT (25.0)
#   - Overweight: true cuando bmi >= 25.0
#   Solo uno de los tres es true.
# Inputs:
#   weight_kg (float), height_m (float)
# Outputs:
#   "BMI: <value>" (round(bmi, 2))
#   "Underweight: true/false"
#   "Normal: true/false"
#   "Overweight: true/false"
# Validations:
#   - Los valores deben poder convertirse a float.
#   - weight_kg > 0 y height_m > 0 (evita dividir entre cero);
#     si no, "Error: invalid input".
# Test cases:
#   1) Normal: weight=70, height=1.75 -> BMI: 22.86 | Underweight: false |
#      Normal: true | Overweight: false
#   2) Border: weight=100, height=2 -> BMI: 25.0 | Underweight: false |
#      Normal: false | Overweight: true (justo 25.0 ya es sobrepeso)
UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0


def problem_6():
    print("--- Problem 6: BMI calculator ---")
    weight_text = input("Enter weight in kg: ")
    height_text = input("Enter height in meters: ")

    try:
        weight_kg = float(weight_text)
        height_m = float(height_text)
    except ValueError:
        print("Error: invalid input")
        return

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
        return

    bmi = weight_kg / (height_m * height_m)
    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT

    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {bool_text(is_underweight)}")
    print(f"Normal: {bool_text(is_normal)}")
    print(f"Overweight: {bool_text(is_overweight)}")


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
# Elegir entre int y float sí importa: los conteos y puntajes son int,
# mientras que el dinero, las temperaturas y las medidas necesitan float.
# Las comparaciones generan booleanos que hacen las decisiones fáciles de leer, y
# guardarlos en variables como has_overtime deja documentadas las reglas.
# Convertir la entrada con try/except ValueError evita que el programa
# truene cuando el usuario escribe texto en lugar de un número.
# Validar rangos (income > 0, height > 0) evita la división entre cero y
# resultados imposibles, como temperaturas debajo del cero absoluto.
# Las constantes con nombre hacen que las reglas sean fáciles de cambiar, y redondear a 2
# decimales deja claras las cantidades de dinero.

# REFERENCIAS
# 1) Documentación oficial de Python - Built-in Types: Numeric Types (int, float).
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Documentación oficial de Python - Built-in Types: Truth Value Testing and Comparisons.
#    https://docs.python.org/3/library/stdtypes.html#comparisons
# 3) Tutorial oficial de Python - An Informal Introduction to Python: Numbers.
#    https://docs.python.org/3/tutorial/introduction.html#numbers
# 4) Tutorial oficial de Python - Errors and Exceptions (try/except ValueError).
#    https://docs.python.org/3/tutorial/errors.html
# 5) PEP 8 - Style Guide for Python Code (guía de estilo de Python).
#    https://peps.python.org/pep-0008/
# 6) W3Schools - Python Numbers.
#    https://www.w3schools.com/python/python_numbers.asp
# 7) Real Python - Numbers in Python.
#    https://realpython.com/python-numbers/
