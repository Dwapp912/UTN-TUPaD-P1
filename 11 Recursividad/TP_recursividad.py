# Trabajo Práctico 11: Aplicación de la Recursividad - Máximo Ponce - Comisión 4

# Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número para calcular factoriales hasta ese número: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

# Ejercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese una posición para mostrar la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()

# Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"Binario: {binario if binario else '0'}")

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
print("Es palíndromo." if es_palindromo(palabra.lower()) else "No es palíndromo.")

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número para sumar sus dígitos: "))
print(f"Suma de los dígitos: {suma_digitos(numero)}")

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
