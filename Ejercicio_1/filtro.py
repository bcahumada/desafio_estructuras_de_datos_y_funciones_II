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

import sys

def filtrar_productos(precios, umbral, operacion='mayor'):
    if operacion not in ['mayor', 'menor']:
        return "Lo sentimos, no es una operación válida"
    
    if operacion == 'mayor':
        productos_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
    elif operacion == 'menor':
        productos_filtrados = [producto for producto, precio in precios.items() if precio < umbral]
    
    if not productos_filtrados:
        return "Lo sentimos. No hay productos en esta categoría"
    
    return f"Los productos {operacion}es al umbral son: " + ', '.join(productos_filtrados)

if __name__ == "__main__":
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    # Verifica si se proporcionó el umbral como argumento
    if len(sys.argv) < 2:
        
        # Solicita al usuario que ingrese el umbral
        umbral = int(input("Por favor, ingrese el umbral para el precio de los productos que desea filtrar: "))
    else:
        umbral = int(sys.argv[1])

    # Verifica si se proporcionó la operación como segundo argumento
    if len(sys.argv) == 3:
        operacion = sys.argv[2]
        print(filtrar_productos(precios, umbral, operacion))
    else:
        print(filtrar_productos(precios, umbral))

