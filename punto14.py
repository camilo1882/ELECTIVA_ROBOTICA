import numpy as np
import matplotlib.pyplot as plt

V = float(input("Ingrese el valor del voltaje (V): "))
C = float(input("Ingrese el valor de la capacitancia (microfaradios): "))
R = float(input("Ingrese el valor de la resistencia (ohmios): "))

#convertir en faradios
Cf=C * 1e-6 
#valor de tiempo
t = np.linspace(0, 5 * R * Cf, 20)

# ecuaciones tau, carga y descarga 
tao = R*Cf
carga = V * (1 - np.exp(-t / tao))
descarga = V * np.exp(-t / tao)
componentes= [V,Cf,R,t]

# Graficar
plt.figure(figsize=(6, 3))
plt.plot(t, carga, label='Carga', color='blue',marker="x")
plt.plot(t, descarga, label='Descarga', color='red',marker="o")
plt.title('Carga y descarga de un circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.show()