''' Listas
Ejercicio N° 1
Crea una lista llamada "frutas" que contenga las
siguientes frutas: manzana, banana, naranja y
pera.
Imprime en pantalla la lista completa'''

lista_de_frutas = ["manzana","banana","naranja","pera"]
print(lista_de_frutas)

'''Ejercicio N° 2
En base al ej 1
Accede al segundo elemento de la lista "frutas" e
imprímelo en pantalla.'''

print(lista_de_frutas[1])

print("Ejercicio N° 3")
'''En base al ej 1
Modifica el primer elemento de la lista "frutas" y
cámbialo por "Cereza".
Imprime en pantalla la lista actualizada.'''

lista_de_frutas[0] = "Cereza"
print(lista_de_frutas)

print("Ejercicio N° 4")
'''En base al ej 1
Agrega la fruta "sandía" al final de la lista
"frutas" utilizando el método append().
Imprime en pantalla la lista actualizada.'''

lista_de_frutas.append("sandia")
print(lista_de_frutas)

print("Ejercicio N° 5")
'''En base al ej 1
Elimina la fruta "naranja" de la lista "frutas"
utilizando el método remove().
Imprime en pantalla la lista resultante.'''

lista_de_frutas.remove("naranja")
print(lista_de_frutas)

print("Ejercicio N° 6")
'''Crea una lista de números llamada "numeros"
con valores del 1 al 5.
Utiliza un bucle for para recorrer la lista e
imprimir en pantalla cada número.'''
#listaf = ["fresa","coca"]
#for x in listaf:
#    print(x)

number_list = [1,2,3,4,5]
for i in lista_de_frutas:
    print(i) 

print("Ejercicio N° 7")
'''Crea una lista llamada "pares" con los números
pares del 2 al 10.
Utiliza el método reverse() para invertir el orden
de los elementos en la lista.
Utiliza el método sort() para ordenar la lista de
forma ascendente.
Imprime en pantalla la lista resultante.'''

pares =[2,3,4,5,6,7,8,9,10]
pares.reverse()
print(pares)
pares.sort()
print(pares)

print("Ejercicio N° 8")
'''Crea una lista llamada "cuadrados" que
contenga los cuadrados de los números del 1 al
5.
Utiliza la comprensión de listas para generar la
lista de forma concisa.
Imprime en pantalla la lista resultante.'''

cuadrados = [n**2 for n in range(1, 6)]
print(cuadrados)

print("Ejercicio N° 9")
'''Crea una lista llamada "nombres" con varios
nombres de personas.
Pide al usuario que ingrese un nombre y verifica
si está presente en la lista.
Muestra un mensaje en pantalla indicando si el
nombre está o no en la lista.'''

nombres = ["Antonela","Claudia","Cristian","Nelson","Milagros"]
n = input('Ingrese un nombre: ')
if n in nombres:
    print(n,"Esta en la lista")
else:
    print(n, "no esta en la lista")
print("")

print("Ejercicio N° 10")
'''Crea una lista llamada "numeros" con valores
del 1 al 10.
Divide la lista en sublistas de tamaño 3
utilizando la técnica de slicing.
Imprime en pantalla las sublistas resultantes.'''

numeros = [1,2,3,4,5,6,7,8,9,10]
subList1 = numeros [1:4]
print(subList1)
subList2 = numeros [4:7]
print(subList2)
subList3 = numeros [7:10]
print(subList3)




