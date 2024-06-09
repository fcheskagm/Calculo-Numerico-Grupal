import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline, RBFInterpolator

# ... (rest of the code remains the same)
# Supongamos que estas son las temperaturas diarias en grados Celsius
temperaturas_diarias = [22, 24, 23, 25, 24, 26, 27]
# Seleccionamos el día 4 como el punto central
dia_central = 4
temperatura_central = temperaturas_diarias[dia_central - 1]

# Estimamos las derivadas usando diferencias finitas
# Para este ejemplo, usaremos diferencias hacia adelante y hacia atrás
f_prima = (temperaturas_diarias[dia_central] - temperaturas_diarias[dia_central - 2]) / 2
f_doble_prima = (temperaturas_diarias[dia_central] - 2 * temperatura_central + temperaturas_diarias[dia_central - 2]) / 2

# Función de interpolación de Taylor
def interpolacion_taylor(x):
    # x es el día para el cual queremos estimar la temperatura
    return (temperatura_central +
            f_prima * (x - dia_central) +
            f_doble_prima * (x - dia_central)**2 / 2)

# Usamos la función para estimar la temperatura en los días 1 al 7
for dia in range(1, 8):
    temperatura_estimada = interpolacion_taylor(dia)
    print(f"Temperatura estimada para el día {dia}: {temperatura_estimada:.2f} °C")

import matplotlib.pyplot as plt

# Datos de temperatura media para los primeros 7 días
temperaturas_media = [28, 28, 27, 27, 28, 28, 29]

# Generamos puntos para la gráfica de la interpolación
dias = list(range(1, 8))
temperaturas_interpoladas = [interpolacion_taylor(dia) for dia in dias]

# Graficamos los datos originales
plt.scatter(dias, temperaturas_media, color='red', label='Datos Originales')

# Graficamos la interpolación de Taylor
plt.plot(dias, temperaturas_interpoladas, color='blue', label='Interpolación de Taylor')

# Añadimos título y leyenda al gráfico
plt.title('Interpolación de Taylor de Temperaturas Diarias')
plt.xlabel('Día')
plt.ylabel('Temperatura (°C)')
plt.legend()

# Mostramos el gráfico
plt.show()