import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Función para determinar el tipo de sistema
#def tipo_sistema(zeta):
#    if zeta < 1:
#        return "Subamortiguado"
#   elif zeta == 1:
#        return "Críticamente amortiguado"
#   else:
#       return "Sobreamortiguado"

# Solicitar al usuario que ingrese los coeficientes
num = [1]  # El numerador siempre es 1 para una función de transferencia de segundo orden
deno = float(input("Ingrese el coeficiente de s^2: "))
deno1= float(input("Ingrese el coeficiente de s: "))
deno2= float(input("Ingrese el coeficiente independiente: "))

# Calcular la frecuencia natural (omega_n) y la relación de amortiguamiento (zeta)
omega_n = np.sqrt(deno2)
zeta = deno1/ (2 * omega_n)

# Determinar el tipo de sistema
tipo = zeta

if zeta < 1:
    print("Subamortiguado")
elif zeta == 1:
    print ("Críticamente amortiguado")
else:
    print  ("Sobreamortiguado")
matriz=[deno,deno1,deno2]

# Calcular la respuesta al escalón del sistema
t = np.linspace(0, 20, 1000)
t, y = signal.step((num, matriz), T=t)

# Graficar la respuesta al escalón
plt.plot(t, y)
plt.title('Respuesta al escalón del sistema ')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.grid(True)
plt.show()