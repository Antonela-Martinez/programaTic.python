print("Ejercicio N° 1")
'''Crea una tupla llamada "meses" que contenga
los nombres de los meses del año como
elementos.
Imprime en pantalla la tupla completa.'''

meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
print(meses)

print("Ejercicio N° 2")
'''En base al ej.1
Accede al tercer elemento de la tupla "meses" e
imprímelo en pantalla.'''

print(meses[2])

print("Ejercicio N° 3")
'''Accede al último elemento de la tupla "meses"
utilizando indexación negativa.
Imprime en pantalla el último elemento.'''

print(meses[-1])

print("Ejercicio N° 4")
'''Intenta asignar un nuevo valor a uno de los
elementos de la tupla "meses" y observa el error
que se produce.
Comenta el código erróneo y explica en un
comentario por qué ocurre el error.'''
#La tupla al ser una estructura de datos inmutable, al querer modificala nos genera un error <no soporta asignacion de objeto>
#meses[3] = "Agosto"
#print(meses)

print("Ejercicio N° 5")
'''Crea dos tuplas llamadas "tupla1" y "tupla2" con
diferentes elementos.
Concatena las dos tuplas y almacena el resultado
en una nueva tupla llamada
"tupla_concatenada".
Imprime en pantalla la tupla concatenada.'''

tupla1 = (1,2,3,4,5,)
tupla2 = (6,7,8)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

print("Ejercicio N°6")
'''Crea una tupla llamada "coordenadas" que
contenga las coordenadas x, y, z de un punto en
el espacio.
Utiliza el desempaquetado de tuplas para
asignar cada valor de la tupla a variables
individuales llamadas "x", "y" y "z".
Imprime en pantalla los valores de las variables.'''

coordenadas = (45, 79, 23)
x, y, z = coordenadas

print("Valor de x:", x)
print("Valor de y:", y)
print("Valor de z:", z)


print("Ejercicio N° 7")
'''Crea una lista de tuplas llamada "alumnos" que
contenga el nombre y la edad de varios
estudiantes.
Utiliza un bucle para iterar sobre la lista de
tuplas y mostrar en pantalla el nombre y la edad
de cada estudiante.'''
print("")
alumnos = [("laura",24),("Miguel",47),("Ana Julia",18)]

#for x in alumnos:
#    print(x)

for nombre, edad in alumnos:
    print("Nombre:", nombre)
    print("Edad:", edad)
    print()