#Trabajo Practico Máximo Ponce.

#1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#2
cosas = ["pizza", "guitarra", "mate", "pelota", "auriculares"]
print(cosas[-2])

#3
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
# Saca el número más grande de la lista (que era 22)

#6
numeros_saltos = list(range(10, 31, 5))
print(numeros_saltos[:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "camioneta"
autos[2] = "buggy"
print(autos)

#8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
del compras[0][0]
print(compras)

#10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
