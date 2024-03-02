import numpy as np

# declarar variables 

presion= 100000 #pascales
r_vastago= 0.05 #mts
r_embolo= 0.1 #mts

# Ecuaciones 
f_avance= presion*(np.pi*r_embolo**2)
f_retroceso= presion*((np.pi*r_embolo**2)-(np.pi*r_vastago**2))

# Imprimir en pantalla
print (f"La fuerza de avance del cilindro es:{f_avance:.2f} N")
print (f"La fuerza de retroceso del cilindro es: {f_retroceso:.2f} N")
