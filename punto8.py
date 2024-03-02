import random

#pedir numeros por consola
rango = int(input("¿cuantos numeros aleatorios?"))
inicio = int(input("cual es el inicio del rango "))
final = int(input("cual es el fin del rango "))

# Generar y mostrar los números aleatorios
for i in range(rango):
    x = random.randint(inicio, final)
    print(x)
