#Trabajo Practico Estructuras Repetitivas, Máximo Ponce.

# Ejercicio 1
for i in range(0, 101):
    print(i)

# Ejercicio 2
numero = int(input("Ingrese un numero: "))
print(f"La cantidad de digitos que contiene {numero} es {len(str(abs(numero)))}")

# Ejercicio 3
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(min(num1, num2) + 1, max(num1, num2)):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es {suma}")

# Ejercicio 4
suma = 0
while True:
    num = int(input("Ingrese su numero: "))
    if num != 0:
        suma += num
    else:
        print(f"El resultado es {suma}")
        break

# Ejercicio 5
import random
numwin = random.randint(1, 9)
intento = 0
while True:
    numero = int(input("Ingrese un numero del 1 al 9: "))
    intento += 1
    if numero < 1 or numero > 9:
        print("Por favor, ingrese un número dentro del rango de 1 a 9")
        continue
    if numero == numwin:
        print(f"¡Felicidades, lo lograste en {intento} intentos!")
        break
    elif numero > numwin:
        print("Más bajo!")
    else:
        print("Más alto!")

# Ejercicio 6
for i in range(100, -1, -2):
    print(i)

# Ejercicio 7
num = int(input("Ingrese un número mayor a 0: "))
while num <= 0:
    num = int(input("Por favor, ingrese un número mayor a 0: "))
suma = 0
for i in range(1, num):
    suma += i
print(f"La suma de los números comprendidos entre 0 y {num} es: {suma}")

# Ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad = 100

for i in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# Ejercicio 9
suma = 0
cantidad = 100

for i in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    suma += num

media = suma / cantidad
print(f"La media es: {media}")

# Ejercicio 10
numero = int(input("Ingrese un número: "))
invertido = int(str(abs(numero))[::-1])
if numero < 0:
    invertido *= -1
print(f"Número invertido: {invertido}")
