print("Ejercicio N° 1")
'''Escribe una función llamada "saludo" que no
reciba parámetros y y muestre el mensaje
"¡Hola!".
Llama a la función varias veces para probarla'''

def saludo():
    print("Hola")

saludo()
saludo()
saludo()

print("Ejercicio N° 2")
'''Escribe una función llamada "saludo" que reciba
un nombre como parámetro y muestre el
mensaje "¡Hola, [nombre]!".
Llama a la función con diferentes nombres para
probarla'''

def saludo(nombre):
    print("Hola! ",nombre)

saludo("Laura")
saludo("Ramon")
saludo("Pricila")

print("Ejercicio N° 3")
'''Crea una función llamada "suma" que reciba dos
números como parámetros y devuelva la suma
de ambos.
Llama a la función con diferentes pares de
números e imprime el resultado'''

def suma(a,b):
    return a+b
print("La suma es: ", suma(20,34))

print("Ejercicio N° 4")
'''Define una función llamada
"saludo_personalizado" que reciba un nombre y
un saludo opcionalmente. Si no se proporciona
un saludo, debe utilizar "¡Hola" como saludo
predeterminado.
Llama a la función para saludar a diferentes
personas con y sin saludo personalizado.'''

def saludo_personalizado(nombre,saludo="Hola!"):
    print(saludo,nombre)

saludo_personalizado("Clara","Buen día!")
saludo_personalizado("Clara")
saludo_personalizado("Clara","Good morning!!")

print("Ejercicio N° 5")
'''Escribe una función llamada "promedio" que
acepte una cantidad variable de números y
calcule su promedio.
Llama a la función con diferentes conjuntos de
números y muestra el promedio resultante.'''

def promedio():
    num=int(input('Ingrese número'))
    suma=0
    i=0
    while(num!=0):
        suma += num
        i +=1
        num=int(input('Ingrese número'))

    return suma/i

print(promedio())

print("Ejercicio N° 6")
'''Crea una función llamada "factorial" que calcule
el factorial de un número dado.
Utiliza la recursividad para implementar la
función.
Prueba la función con diferentes números y
muestra los resultados.'''

def factorial(numero):
    if(numero<=1):
        return 1
    return numero * factorial(numero-1)

print(factorial(3))
print(factorial(6))

print("Ejercicio N° 7")
'''Escribe una función llamada "ordenar_lista" que
reciba una lista de números y devuelva una
nueva lista con los mismos números ordenados
de forma ascendente.
Utiliza una función integrada de Python para
realizar la clasificación.
Prueba la función con diferentes listas de
números.'''

def ordenar_lista(numerosList):
    return sorted(numerosList)

my_list = [3,6,8,1,9,33,78]
print(ordenar_lista(my_list))

print("Ejercicio N° 8")
'''Define una función llamada "dividir" que acepte
dos números y realice la división del primero por
el segundo.
Maneja la excepción que se produce cuando el
divisor es igual a cero y muestra un mensaje de
error adecuado.
Llama a la función con diferentes pares de
números, incluido el caso en el que el divisor sea
cero.'''

def dividir(a,b):
    try:
        return a/b
    except:
        return print("ERROR: No se puede dividir por cero!!")
    
print(dividir(4,0))

print("Ejercicio N° 9")
'''Crea una función llamada
"informacion_persona" que acepte los
siguientes parámetros: nombre, edad y ciudad.
La función debe imprimir en pantalla la
información proporcionada en un formato
legible, como "Nombre: [nombre], Edad: [edad],
Ciudad: [ciudad]". Llama a la función utilizando
argumentos de palabras clave para especificar
los valores de los parámetros.'''

def informacion_persona(nombre,edad,ciudad):
    informacion = {
        "Nombre":nombre,
        "Edad":edad,
        "Ciudad":ciudad
        }
    return informacion

informacion_persona("Lourdes",23,"Carhue")

print("Ejercicio N° 11")
'''Define una función llamada
"concatenar_strings" que acepte una cantidad
variable de cadenas de texto y las concatene en
una sola cadena.
Utiliza el operador de concatenación de cadenas
o el método join() para realizar la concatenación.
Prueba la función con diferentes cadenas y
muestra el resultado.'''

def concatenar_strings(cadena_list):
    concatenar = ', '.join(cadena_list)
    return concatenar

my_list = ["Romina","Marcela","clara"]
concatenar_strings(my_list)

print("Ejercicio N°12")
'''Escribe una función llamada
"eliminar_duplicados" que reciba una lista como
parámetro y devuelva una nueva lista que
contenga los elementos únicos de la lista
original, sin duplicados.
Utiliza las propiedades de los conjuntos (set)
para eliminar los elementos duplicados.
Prueba la función con diferentes listas y muestra
el resultado.'''

def eliminar_duplicado(my_list):
    return set(my_list)

list = [2,3,5,5,6,2,8,8,9]
eliminar_duplicado(list)

print("Ejercicio N°13")
'''Crea una función recursiva llamada "fibonacci"
que calcule el enésimo número de la secuencia
de Fibonacci.
La secuencia de Fibonacci comienza con 0 y 1, y
cada número siguiente se calcula sumando los
dos números anteriores.
Prueba la función para obtener diferentes
números de la secuencia de Fibonacci.'''

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso
n = 10
resultado = fibonacci(n)
print(f"El número en la posición {n} de la secuencia de Fibonacci es: {resultado}")

print("Ejercicio N°14")
'''Crea una función llamada
"generar_numero_aleatorio" que utilice el
módulo random de Python para generar un
número entero aleatorio entre un rango dado.
El rango debe ser especificado como parámetros
de la función.
Llama a la función para generar diferentes
números aleatorios y muestra los resultados.'''
import random
def generar_numero_aleatorio(n1,n2):
    return random.randint(n1,n2)

generar_numero_aleatorio(2,10)

print("Ejercicio N°15")
'''Escribe una función llamada "contar_lineas" que
acepte el nombre de un archivo como parámetro
y cuente el número total de líneas en ese
archivo.
Utiliza el manejo de archivos en Python para
abrir y leer el archivo.
Llama a la función con diferentes archivos y
muestra el número de líneas resultante.'''

def contar_lineas(direccion_archivo):
    with open(direccion_archivo) as archivo:
            lineas = archivo.readlines()
            total_lineas = len(lineas)
            return total_lineas
    
direccion_archivo = 'ejemplo.py.txt'
resultado = contar_lineas(direccion_archivo)
print(f"El archivo '{direccion_archivo}' tiene {resultado} líneas.")

print("Ejercicio N°16")
'''Escribe una función llamada
"calcular_estadisticas" que reciba una tupla de
números como parámetro y devuelva la suma, el
promedio y el máximo valor de la tupla.
Llama a la función con diferentes tuplas de
números y muestra los resultados obtenidos.'''

def suma(my_tuple):
    sum=0
    for x in my_tuple:
        sum +=x
    return suma
my_tuple = (4,5,7,2,8)
suma(my_tuple)

def calcular_estadisticas(my_tuple):
    return suma(my_tuple),promedio(my_tuple),valor_maximo(my_tuple)

my_tuple = (4,5,7,2,8)
suma,promedio,valor_maximo = calcular_estadisticas(my_tuple)
print(f"La suma es: {suma}, el promedio es: {promedio} y el valor maximo es:{valor_maximo}")

#############################################

def calcular_estadisticas(tupla_numeros):
    suma = sum(tupla_numeros)
    promedio = suma / len(tupla_numeros)
    maximo = max(tupla_numeros)
    return suma, promedio, maximo

# Ejemplo de uso
tupla1 = (1, 2, 3, 4, 5)
resultado1 = calcular_estadisticas(tupla1)
print(f"Suma: {resultado1[0]}, Promedio: {resultado1[1]}, Máximo: {resultado1[2]}")

tupla2 = (10, 20, 30, 40, 50)
resultado2 = calcular_estadisticas(tupla2)
print(f"Suma: {resultado2[0]}, Promedio: {resultado2[1]}, Máximo: {resultado2[2]}")


