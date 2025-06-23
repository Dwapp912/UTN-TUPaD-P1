# Trabajo Práctico 6: Estructuras de Datos Complejas - Máximo Ponce - Comisión 4

# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario actualizado con nuevas frutas:", precios_frutas)

# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Diccionario con precios actualizados:", precios_frutas)

# Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# Ejercicio 4
contactos = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

consulta = input("Ingrese un nombre para buscar su número: ")
if consulta in contactos:
    print(f"Número de {consulta}: {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

# Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print("Cantidad de veces que aparece cada palabra:", conteo_palabras)

# Ejercicio 6
alumnos = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} - Promedio: {promedio:.2f}")

# Ejercicio 7
parcial1 = set(map(int, input("Ingrese los legajos que aprobaron Parcial 1 (separados por espacio): ").split()))
parcial2 = set(map(int, input("Ingrese los legajos que aprobaron Parcial 2 (separados por espacio): ").split()))

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Ejercicio 8
stock = {}
while True:
    producto = input("Ingrese nombre del producto (o 'salir' para terminar): ")
    if producto.lower() == 'salir':
        break
    if producto in stock:
        cantidad = int(input("Ingrese cantidad a agregar: "))
        stock[producto] += cantidad
    else:
        cantidad = int(input("Producto nuevo. Ingrese cantidad inicial: "))
        stock[producto] = cantidad

    print(f"Stock actual de {producto}: {stock[producto]}")

consulta = input("Consultar stock de producto: ")
print(f"Stock de {consulta}: {stock.get(consulta, 'No registrado')}")

# Ejercicio 9
agenda = {}
while True:
    dia = input("Día (o 'fin' para salir): ")
    if dia.lower() == 'fin':
        break
    hora = input("Hora: ")
    evento = input("Descripción del evento: ")
    agenda[(dia, hora)] = evento

dia_consulta = input("Consultar agenda - Día: ")
hora_consulta = input("Consultar agenda - Hora: ")
print("Evento:", agenda.get((dia_consulta, hora_consulta), "No hay evento agendado."))

# Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Italia": "Roma",
    "Japón": "Tokio"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido (capitales como claves):", capitales_paises)
