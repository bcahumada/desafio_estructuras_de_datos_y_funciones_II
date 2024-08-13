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



def factorial(n):
    '''Funcionamiento: Inicializa una variable resultado en 1.
Usa un bucle for que comienza en 2 y se extiende hasta n inclusive (range(2, n+1)).
En cada iteración, multiplica resultado por el valor de i, acumulando el producto.
Devuelve el resultado final, que es el factorial de n.
Ejemplo: Si n es 5, el cálculo será 1 * 2 * 3 * 4 * 5, que da como resultado 120'''
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def productoria(lista):
    '''Funcionamiento: Inicializa una variable resultado en 1.
Usa un bucle for para recorrer cada elemento num en la lista.
En cada iteración, multiplica resultado por num, acumulando el producto.
Devuelve el resultado final, que es la productoria de los elementos en la lista.
Ejemplo: Si la lista es [3, 6, 4, 2, 8], el cálculo será 1 * 3 * 6 * 4 * 2 * 8, que da como resultado 1152.'''
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def calcular(**kwargs):
    '''Funcionamiento: La función calcular acepta un número variable de argumentos con nombre (kwargs).
Recorre cada par key, value en kwargs.items().
Si la clave (key) contiene la subcadena 'fact', llama a la función factorial con el valor asociado y muestra el resultado.
Si la clave contiene la subcadena 'prod', llama a la función productoria con el valor asociado (que debe ser una lista) y muestra el resultado.
Ejemplo:
Para calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6), la función:
Calcula el factorial de 5 (120) y de 6 (720).
Calcula la productoria de [3, 6, 4, 2, 8] (1152).'''
    for key, value in kwargs.items():
        if 'fact' in key:
            print(f"El factorial de {value} es {factorial(value)}")
        elif 'prod' in key:
            print(f"La productoria de {value} es {productoria(value)}")

# Ejecución para el ejemplo
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
