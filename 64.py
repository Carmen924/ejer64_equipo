EQUIPO:
Alcantar Cabrera Jose Eduardo 
Cano Sanchez Veronica 
Gutierrez Garcia Lucero
Hernandez Valle Carmen 
# Variables
# 1. Inicializa una variable entera y muestra su valor
entero = 5
print(entero)  


# 2. Inicializa una variable de punto flotante y muestra su valor
flotante = 3.14
print(flotante)  


# 3. Inicializa una cadena y muestra su longitud
nombre = "Python"  
print(len(nombre))  

# 4. Inicializa una lista y muestra su primer elemento
lista = [1, 2, 3]  
print(lista[0])  

# 5. Inicializa un diccionario y muestra un valor por clave
diccionario = {'a': 1, 'b': 2}  
print(diccionario['a'])  

# Condicionales
# 6. Comprobar si un número es par
num = 4
if num % 2 == 0:
    print("Es par") 

# 7. Verificar si una cadena contiene una subcadena
cadena = "Hola Mundo"
if "Mundo" in cadena:
    print("Contiene 'Mundo'") 

# 8. Clasificar un número como positivo, negativo o cero
num = -1
if num > 0:
    print("Positivo")  
elif num < 0:
    print("Negativo")
else:
    print("Cero")

# 9. Comprobar si un año es bisiesto
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Bisiesto")  

# 10. Validar un número de rango
num = 15
if num < 10 or num > 20:
    print("Fuera de rango")  

# Ciclos
# 11. Imprimir números del 1 al 5 usando un bucle for
for i in range(1, 6):
    print(i, end=", ")  
print()

# 12. Sumar los primeros 10 números naturales
suma = sum(range(1, 11))
print(suma)  

# 13. Crear una lista con los cuadrados de los primeros 5 números
cuadrados = [i**2 for i in range(1, 6)]
print(cuadrados)  

# 14. Contar cuántas vocales hay en una cadena
cadena = "Hola"
vocales = "aeiouAEIOU"
contador = sum(1 for letra in cadena if letra in vocales)
print(contador)  

# 15. Imprimir una tabla de multiplicar
numero = 3
for i in range(1, 11):
    print(numero * i, end=", ")  
print()

# Colecciones
# 16. Inicializar una lista vacía y agregar elementos
lista = []
lista.append(1)
print(lista)  
lista.append(2)
print(lista)  

# 17. Crear un conjunto y verificar si un elemento está presente
conjunto = {1, 2, 3}
print(1 in conjunto)  

# 18. Crear un diccionario y agregar un par clave-valor
diccionario = {}
diccionario['a'] = 1
print(diccionario)  

# 19. Ordenar una lista
lista = [3, 1, 2]
lista.sort()
print(lista)  

# 20. Obtener la longitud de una lista
lista = [1, 2, 3]
print(len(lista))  

# Ejercicios combinados
# 21. Sumar elementos de una lista
lista = [1, 2, 3, 4, 5]
suma = sum(lista)
print(suma)  

# 22. Filtrar números pares de una lista
lista = [1, 2, 3, 4, 5]
pares = [num for num in lista if num % 2 == 0]
print(pares)  

# 23. Contar la cantidad de palabras en una cadena
cadena = "Hola Mundo"
cantidad_palabras = len(cadena.split())
print(cantidad_palabras) 

# 24. Encontrar el valor máximo en una lista
lista = [1, 3, 2]
print(max(lista)) 

# 25. Verificar si todos los elementos de una lista son verdaderos
lista = [True, True, False]
print(all(lista))  

# 26. Comprobar si hay al menos un elemento verdadero
lista = [False, False, True]
print(any(lista))  

# 27. Crear un nuevo diccionario a partir de dos listas
claves = ['a', 'b', 'c']
valores = [1, 2, 3]
diccionario = dict(zip(claves, valores))
print(diccionario) 


# 28. Crear una lista de tuplas a partir de dos listas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista_de_tuplas = list(zip(lista1, lista2))
print(lista_de_tuplas)  

# 29. Contar la cantidad de apariciones de un elemento en una lista
lista = [1, 2, 1, 3]
apariciones = lista.count(1)
print(apariciones) 

# 30. Generar una lista de Fibonacci
n = 5
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci[:n])  

# 31. Reversar una lista
lista = [1, 2, 3]
lista.reverse()
print(lista)  

# 32. Concatenar dos listas
lista1 = [1, 2]
lista2 = [3, 4]
concatenada = lista1 + lista2
print(concatenada) 

# 33. Crear una lista de números aleatorios
import random
numeros_aleatorios = random.sample(range(1, 11), 5)
print(numeros_aleatorios)  

# 34. Contar la cantidad de elementos en un conjunto
conjunto = {1, 2, 3}
print(len(conjunto))  

# 35. Crear un diccionario a partir de una lista de tuplas
tuplas = [(1, 'a'), (2, 'b')]
diccionario = dict(tuplas)
print(diccionario)  

# 36. Obtener los elementos únicos de una lista
lista = [1, 2, 2, 3]
unicos = list(set(lista))
print(unicos)  

# 37. Verificar si un diccionario contiene una clave
diccionario = {'a': 1}
print('a' in diccionario)  

# 38. Fusionar dos diccionarios
dic1 = {'a': 1}
dic2 = {'b': 2}
fusionado = {**dic1, **dic2}
print(fusionado)  

# 39. Convertir una lista en un conjunto
lista = [1, 2, 2, 3]
conjunto = set(lista)
print(conjunto) 

# 40. Obtener los elementos de un diccionario en forma de lista
claves=list(diccionario.keys())
valores =list(diccionario.values())

print("Claves:", claves)
print("Valores:", valores)

# 41. Calcular la suma de los valores en un diccionario
diccionario = {'a': 1, 'b': 2}
suma_valores = sum(diccionario.values())  

# 42. Filtrar un diccionario por un valor mínimo
diccionario = {'a': 1, 'b': 2, 'c': 3}
filtrado = {k: v for k, v in diccionario.items() if v >= 2}  

# 43. Crear un contador de palabras
from collections import Counter
cadena = "Hola mundo hola"
contador = Counter(cadena.split())  

# 44. Obtener los elementos comunes entre dos listas
lista1 = [1, 2, 3]
lista2 = [2, 3, 4]
comunes = list(set(lista1) & set(lista2))  

# 45. Comprobar si una lista es un subconjunto de otra
lista1 = [1, 2]
lista2 = [1, 2, 3]
subconjunto = set(lista1).issubset(set(lista2))  

# 46. Generar una lista de números pares del 1 al 20
numeros_pares = [i for i in range(1, 21) if i % 2 == 0]  

# 47. Crear un diccionario de frecuencias de una lista
lista = [1, 2, 2, 3]
frecuencias = {x: lista.count(x) for x in set(lista)} 

# 48. Unir dos listas alternando sus elementos
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
unido = [elem for pair in zip(lista1, lista2) for elem in pair]  

# 49. Encontrar el índice de un elemento en una lista
lista = [1, 2, 3]
indice = lista.index(2)  

# 50. Crear un diccionario a partir de una lista de claves y valores
claves = ['a', 'b']
valores = [1, 2]
diccionario_creado = dict(zip(claves, valores))  

# 51. Filtrar palabras largas de una lista
palabras = ["uno", "dos", "tres", "cuatro"]
filtradas = [palabra for palabra in palabras if len(palabra) > 3] 

# 52. Crear una lista de los índices de los elementos en una lista
lista = [10, 20, 30]
indices = list(range(len(lista)))  

# 53. Ordenar un diccionario por sus valores
diccionario = {'a': 3, 'b': 1, 'c': 2}
ordenado = dict(sorted(diccionario.items(), key=lambda item: item[1])) 

# 54. Verificar si dos listas son iguales
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
son_iguales = lista1 == lista2  

# 55. Crear un conjunto a partir de una lista con duplicados
lista = [1, 1, 2, 3]
conjunto = set(lista)  

# 56. Calcular el promedio de una lista
lista = [1, 2, 3, 4, 5]
promedio = sum(lista) / len(lista)  

# 57. Comprobar si una lista está vacía
lista = []
esta_vacia = len(lista) == 0  

# 58. Obtener los elementos únicos de una lista manteniendo el orden
lista = [1, 2, 2, 3]
unicos = []
for item in lista:
    if item not in unicos:
        unicos.append(item)  

# 59. Contar las letras en una cadena
cadena = "Hola"
contador_letras = {letra: cadena.count(letra) for letra in set(cadena)}

# 60. Cambiar el valor de un elemento en un diccionario
diccionario = {'a': 1}
diccionario['a'] = 2  # {'a': 2}

# 61. Eliminar un elemento de una lista
lista = [1, 2, 3]
lista.remove(2)  # [1, 3]

# 62. Repetir una cadena varias veces
cadena = "Hola"
repetida = cadena * 3  

# 63. Crear una lista de números aleatorios y ordenarla
import random
numeros_aleatorios = random.sample(range(1, 101), 10)  # lista de 10 números aleatorios entre 1 y 100
numeros_aleatorios.sort()  

# 64. Crear una lista de listas
lista_de_listas = [[1, 2], [3, 4]]
print(lista_de_listas)
