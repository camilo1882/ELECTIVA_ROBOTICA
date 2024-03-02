import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicitar al usuario que ingrese las coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origen
ax.quiver(0, 0, 0, x, y, z, color='red', arrow_length_ratio=0.05)

# Configurar límites
ax.set_xlim([0, max(1, abs(x))])
ax.set_ylim([0, max(1, abs(y))])
ax.set_zlim([0, max(1, abs(z))])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.grid(True)
plt.title('Vector en un sistema de coordenadas XYZ')
plt.show()