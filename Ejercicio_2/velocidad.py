# Contexto:

# Una empresa de flotas debe medir mediante telemetría las velocidades de cada una de sus correas transportadoras. 
# Una de sus políticas es distribuir su energía de manera eficiente, por lo que, para poder entregar energía a las correas más lentas, 
# es necesario ralentizar las más rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se requiere 
# levantar una alerta de la posición de las correas transportadoras que están por sobre el promedio.

# Requerimiento:

# Determinar una funcionalidad que calcule el promedio de una lista de velocidades. 
# El servidor donde se pretende instalar esta funcionalidad no cuenta con mucha capacidad por lo que se pide no depender de librerías externas.
# Listar las posiciones de todas las correas transportadoras que están sobre el promedio.

# Ejecución y Output esperado:

# Comando: python velocidad.py
# Output: [0, 2, 3, 6, 8, 9, 10, 13, 15, 17, 18, 19, 20, 22, 24, 29, 30, 31, 32, 34, 35, 36, 37, 41, 48, 52, 54, 56, 57, 58, 59]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Solución

# Siendo: 

# i: Índice de la lista velocidades. Este índice se obtiene usando la función enumerate, 
# que devuelve tanto el índice como el valor correspondiente del elemento en la lista.

# v: Valor de la velocidad en la lista velocidades en la posición i. Es decir, v es el valor 
# de la velocidad correspondiente al índice i.



def alertas_telematicas(velocidades):
    promedio = sum(velocidades) / len(velocidades)
    return [i for i, v in enumerate(velocidades) if v > promedio]

# Lista de prueba
velocidades = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 
               23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

# Cálculo del promedio
promedio = sum(velocidades) / len(velocidades)

# Ejecución
print(f"La velocidad promedio de las correas es de: {promedio}")
print(alertas_telematicas(velocidades))
