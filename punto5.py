import numpy as np

#estructura de funciones 

def rotacion_x():
    radianes = np.radians(60)
    mov=np.array([
        [1, 0, 0],
        [0, np.cos(radianes), -np.sin(radianes)],
        [0, np.sin(radianes), np.cos(radianes)]
    ])
    print("\nMatriz de rotación en el eje X:")
    print (mov)

def rotacion_y():
    radianes = np.radians(30)
    mov2=np.array([
        [np.cos(radianes), 0, np.sin(radianes)],
        [0, 1, 0],
        [-np.sin(radianes), 0, np.cos(radianes)]
    ])
    print("\nMatriz de rotación en el eje Y:")
    print (mov2)

def rotacion_z():
    radianes = np.radians(0)
    mov3= np.array([
        [np.cos(radianes), -np.sin(radianes), 0],
        [np.sin(radianes), np.cos(radianes), 0],
        [0, 0, 1]
    ])
    print("\nMatriz de rotación en el eje Z:")
    print(mov3)

# llamado de funciones 
    
print(rotacion_x())    
print(rotacion_y())
print(rotacion_z())
