import numpy as np
import matplotlib.pyplot as plt

# rango de temperatura
T = np.linspace(-200, 200, 2)  # Genera 1000 puntos entre -200°C y 200°C

Ro=100 #temperatura 0 en ohms
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
R = Ro * (1 + A * T + B * T**2 + C * (T - 100) * T**3)

# Graficar
plt.figure(figsize=(6, 3))
plt.plot(T, R, color='pink')
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohm)')
plt.grid(True)
plt.show()