import numpy

#creacionn de variables 

vector1 = numpy.array ([1,2])
vector2 = numpy.array ([4,5])

#Operaciones entre vectores 

suma= vector1+vector2
resta= vector1-vector2
division= vector1/vector2
oper1= vector1[0]*vector2[0] 
oper2= vector1[1]*vector2[1]
oper3= vector1[0]*vector2[1] 
oper4= vector1[1]*vector2[0]

#Imprimir en pantalla
print(" Vector #1=",vector1,"\n","Vector #2=",vector2,"\n") 
print(f"La suma de dos vectores es: {suma}")
print(f"La resta de dos vectores es: {resta}")
print(f"La division de dos vectores es:[{division[0]:.2f} {division[1]:.2f}]") 
print(f"producto punto de dos vectores es= {oper1+oper2}") 
print(f"producto cruz de dos vectores es= {oper3-oper4}") 

