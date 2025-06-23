# Trabajo Practico Máximo Ponce - Funciones

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4a. Función que calcula el área del círculo
def calcular_area_circulo(radio):
    pi = 3.1416
    return pi * radio ** 2

# 4b. Función que calcula el perímetro del círculo
def calcular_perimetro_circulo(radio):
    pi = 3.1416
    return 2 * pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar de un número del 1 al 10
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que devuelve suma, resta, multiplicación y división como tupla
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: división por cero"
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

# 9. Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# -------------------- Programa principal --------------------

# 1
imprimir_hola_mundo()

# 2
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# 3
nombre_p = input("Ingrese su nombre: ")
apellido_p = input("Ingrese su apellido: ")
edad_p = input("Ingrese su edad: ")
residencia_p = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre_p, apellido_p, edad_p, residencia_p)

# 4
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# 5
segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# 6
numero_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# 7
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {mult}")
print(f"División: {div}")

# 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc}")

# 9
celsius = float(input("Ingrese temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10
num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))
num3 = float(input("Ingrese tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio es: {promedio:.2f}")
