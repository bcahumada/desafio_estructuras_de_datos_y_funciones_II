# Contexto

# La empresa presta soporte es a las ONG. 
# En un programa de ayuda escolar que tiene la esta ONG se está enseñando a programar algunas operaciones
# avanzadas a niños con alto potencial pero de escasos recursos. 

# Requerimiento: 
# Una función que calcule el factorial.
# Una función que calcule la productoria.
# Una función que permita controlar los cálculos. Esta función se debe invocar de la siguiente manera:
# calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

# El factorial se define de la siguiente forma:
# 𝑛! = 𝑛 * 𝑛 −1 * 𝑛 − 2 * . * 2 * 1

# En un ejemplo práctico, el factorial de 5 (5!) se calculará como:
# 5! = 5 * 4 * 3 * 2 * 1 = 120
 
# Por otro lado la productoria se define como la multiplicación de elementos.
# 𝐴 = [3,6,4,2,8]
# ∏𝐴𝑖  =  3 * 6 * 4 * 2 * 8
 


# Se ingresarán un valor numérico como argumento con el nombre fact_i cuando se requiera calcular un factorial, 
# y una lista como argumento prod_i cuando se requiera calcular una  productoria. 

# Cabe destacar que la función debe permitir ingresar estos argumentos en cualquier orden y en cualquier cantidad. 
# El resultado de la función se debe imprimir en pantalla de la siguiente forma:
# El factorial de 5 es 120
# La productoria de [4, 6, 7, 4, 3] es 2016
# El factorial de 6 es 720
#----------------------------------------------------------------------------------------------------------------------#

# Solución

import math
from functools import reduce


# Función que calcula el factorial de un número
'''Calcula el factorial de n usando la función math.factorial().'''
def calcular_factorial(n):
    return math.factorial(n)


# Función que calcula la productoria de una lista
'''Calcula la productoria de los elementos en la lista lista utilizando reduce() y una función lambda.'''
def calcular_productoria(lista):
    return reduce(lambda x, y: x * y, lista)


# Función que permite controlar los cálculos
'''Esta es la función principal que toma argumentos de tipo keyword (fact_1, prod_1, fact_2, etc.).

Recorre los argumentos usando un bucle for.
Si el argumento empieza con "fact_", calcula el factorial.
Si el argumento empieza con "prod_", calcula la productoria.
Si el argumento tiene un nombre no reconocido, muestra un mensaje de error.'''
def calcular(**kwargs):
    for key, value in kwargs.items():
        if key.startswith("fact_"):
            resultado = calcular_factorial(value)
            print(f"El factorial de {value} es {resultado}")
        elif key.startswith("prod_"):
            resultado = calcular_productoria(value)
            print(f"La productoria de {value} es {resultado}")
        else:
            print(f"El argumento {key} no es válido")

# Ejemplo de ejecución
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)


