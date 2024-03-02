import numpy as np

def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return base * altura * (1/3)

def volumen_cono_trun(rbase_mayor, rbase_menor, altura):
    return (1/3) * altura * np.pi * (rbase_mayor**2 + rbase_menor**2+ rbase_mayor * rbase_menor)

def volumen_cilindro(radio, altura):
    return np.pi * radio**2 * altura

print("Escoja la opcion que desee")
print("1- Prisma")
print("2- Piramide")
print("3- Cono truncado")
print("4- Cilindro")

pregunta="s"

while pregunta != "n":

    opcion=int(input("Que opcion desea: "))

    if opcion == 1:
        base=(float(input("Medida de la base del prisma: ")))
        altura=(float(input("ALtura de la figura: ")))
        print("La piramide tiene un volumen de :",volumen_prisma(base, altura))

    elif opcion == 2:

        base=(float(input("Medida de la base de la piramide: ")))
        altura=(float(input("ALtura de la piramide: ")))
        print("La piramide tiene un volumen de : ",volumen_piramide(base, altura))

    elif opcion == 3:
        rbase_mayor=(float(input("Ingrese radio mayor de la figura: ")))
        rbase_menor=(float(input("Ingrese radio menor de la figura: ")))
        altura=(float(input("ingrese altura de la figura: ")))
        print("El volumen del cono truncado es de: ", volumen_cono_trun(rbase_mayor, rbase_menor,altura))

    elif opcion == 4:
        radio=(int(input("Escriba el radio de la figura")))
        altura=(int(input("Ingrese altura de la figura")))
        print("El volumen del cilindro es: ",volumen_cilindro(radio,altura))
    
    pregunta = input('Desea continuar (s/n) \n')
print("Termino el programa")

    