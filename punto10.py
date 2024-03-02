def cilindrico():
    print("ROBOT CILINDRICO")
    print("Este cuenta con:")
    print("1 Articulacion de rebolucion\n2 Prismaticas")

def cartesiano():
    print("ROBOT CARTESIANO")
    print("Este cuenta con:")
    print("3 articulaciones prismaticas o deslizantes")

def esferico():
    print("ROBOT ESFERICO")
    print("Este cuenta con:")      
    print("2 articulaciones rotacionales \n1 Lineal")  

print (f"___MENU___")
print(f"1- Cilindrico")
print(f"2- Cartesiano")
print(f"3- Esferico")

pregunta="s"

while pregunta != "n":

    opcion=int(input("Que opcion desea: "))

    if opcion == 1:
        print (cilindrico())
    if opcion == 2:
        print (cartesiano())
    if opcion == 3:
        print (esferico())
    
    pregunta = input('Desea continuar (s/n) \n')
print("Termino el programa")