#1
edad=int(input("Ingrese su edad: "))
if edad >= 18: 
    print ("Eres mayor de edad")
else:
    print("Eres menor de edad") 

#2
nota=int(input("Ingrese su nota: "))
if nota >=6 and nota <= 10:
    print ("Estas aprobado!")
elif nota >= 11:
    print("Ingresa una nota entre 1 y 10")
else:
    print("Desaprobado rey")

#3
while True:
    numero=int(input("ingrese un numero: "))
    if numero %2 == 0:
        print("Ingresaste un numero par")
        break
    else:
        print("Por favor, Ingrese un numero par")
        
    
#4
edad=int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto mayor")

#5
contraseña=input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if len(contraseña) >=8 and len(contraseña) <=14:
    print("Su contraseña ha sido ingresada correctamente")
else:   
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar un sesgo claro.")

#7
palabra=input("Ingrese una palabra: ")
if palabra[-1]in "aeiouAEIOU":
    print(f"{palabra}!")
else:
    print(F"{palabra}")


#8
nombre=input("Ingrese su nombre: ")
opcion=input("Elija la opcion '1', '2' o '3': ")
if opcion == "1" :
    print (nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif "3":
    print(nombre.title())
    
#9
magnitud=int(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("leve")
elif magnitud < 5:
    print("moderado")
elif magnitud < 6:
    print("fuerte")
elif magnitud < 7:
    print("muy fuerte")
elif magnitud >= 7:
    print("extremo")

#10
hemisferio = input("Ingrese el hemisferio (N para norte, S para sur): ").upper()
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")

else:
    print("Hemisferio no válido. Use 'N' o 'S'.")
