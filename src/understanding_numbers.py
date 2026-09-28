
# Numeros
# Numeros - Itegrales 

"""
Los numeros enteros los podemos
sumar (+), restar (-), multiplicar (*)
y dividir (/)
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2)

print(3**2) #3^2
print(3**3) #3^3
print(10**6) #10^6
print(10%2) #Modulo (mod)
age = 34
print(age)

print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

# Edad de prof. charly
# message = "charly tiene " + age + " años." Error
age = 34
message = "charly tiene " + str(age) + " años."
print(message)

#TypeError
"""
TypeError: python no puede reconocer el tipo de 
infotmacion que se esta utilizando.
"""

message_f = f"charly tiene {age} años."
print(message_f)

# Metodo build-in type()
print(type(age),type("holap"), type(0.54), type(True))