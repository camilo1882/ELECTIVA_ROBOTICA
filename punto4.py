#Segun ecucacion de callenadar van dusen 
# R= R0+(1+A*T+B*T^2+C*(T-100)*T^3)

Ro=100 #temperatura 0 en ohms
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
T=100
R = Ro * (1 + A * T + B * T**2 + C * (T - 100) * T**3)
print (f"Para llegar a una temperatura de {T}°C, se necesita una resistencia de {R:.3f} ohms")



