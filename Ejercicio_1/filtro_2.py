# Contexto:

# Ejercicio 1. Filtrado relevante:
# La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar
# un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al
# problema. Dada una muestra de los productos que actualmente se encuentran disponibles
# en la tienda (un diccionario), se solicita implementar una función que permita entregar lo
# siguiente:

# Un diccionario con los productos que cumplen una cierta condición dado un umbral
# La función debe permitir mostrar los valores mayor que o menor que un umbral (siempre estrictos).
# Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos que se indique lo contrario.

# Para desarrollar la funcionalidad se le entrega un diccionario de prueba para verificar sus resultados.

# precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}

#--------------------------------------------------------------------------------------------------------------------------------------------#

# Ejecución

# Se espera ejecutar el programa de la siguiente manera:
# Si se especifica un argumento, este debe ser el umbral y por defecto debe calcular los que son estrictamente mayores al umbral.

# Ej:  python filtro.py 30000
# Output: Los productos mayores al umbral son: Notebook, Monitor, Escritorio, Tarjeta de Video
#--------------------------------------------------------------------------------------------------------------------------------------------#
# Solución

# Siendo:
# k: producto
# v: precio

def filtrar_umbral(precios, umbral, condicion='mayor'):
    if condicion == 'mayor':
        return {k: v for k, v in precios.items() if v > umbral}
    elif condicion == 'menor':
        return {k: v for k, v in precios.items() if v < umbral}
    else:
        return "Lo sentimos, no es una operación válida"

# Diccionario de prueba
precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}

# Ejecución
print(filtrar_umbral(precios, 30000))  # Filtrar productos con precio mayor a 30000
print(filtrar_umbral(precios, 30000, 'menor'))  # Filtrar productos con precio menor a 30000
print(filtrar_umbral(precios, 30000, 'otro'))  # Operación no válida