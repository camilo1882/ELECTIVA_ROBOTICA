import numpy as np

def rec_cilindricas(x, y, z):
    r, theta = rec_polares(x, y)
    return r, theta, z

def rec_polares(x, y):
    r = ((x**2 + y**2))**0.5
    theta = np.arctan2(y, x)
    return r, theta

# Coordenadas rectangulares
x = 3
y = 4
z = 2

# Conversión a coordenadas polares
polares= rec_polares(x,y)
print("Coordenadas polares:","\n","--> r=", polares[0],"\n","--> theta =", polares[1],"\n")

# Conversión a coordenadas cilíndricas
cilindricas = rec_cilindricas(x, y, z)
print("Coordenadas cilíndricas:","\n","--> r =", cilindricas[0],"\n", "--> theta =", cilindricas[1],"\n", "--> z =",cilindricas[2])
