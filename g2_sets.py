print("Ejercicio N°1")
'''Crea un conjunto llamado "frutas" que contenga
las siguientes frutas: manzana, plátano, naranja
y pera.
Imprime en pantalla el conjunto completo.'''

frutas = {"manzana","plátano","naranja","pera"}
print(frutas)

print("Ejercicio N°2")
'''Crea dos conjuntos: "frutas1" con las frutas
manzana, plátano y pera, y "frutas2" con las
frutas naranja y sandía.
Realiza las siguientes operaciones e imprime los
resultados:
Unión de los conjuntos frutas1 y frutas2.
Intersección de los conjuntos frutas1 y frutas2.
Diferencia entre los conjuntos frutas1 y frutas2.'''

frutas1 = {"manzana","plátano","pera"}
frutas2 = {"naranja","sandia"}
union = frutas1.union(frutas2)
print("La union es: ",union)
intersection = frutas1.intersection(frutas2)
print("La interseccion es: ", intersection)
diference = frutas1 - frutas2
print("La diferencia es: ",diference)

print("Ejercicio N°3")
'''Crea un conjunto vacío llamado "numeros".
Agrega los números del 1 al 5 al conjunto
utilizando el método add().
Elimina el número 3 del conjunto utilizando el
método remove() o discard().
Imprime en pantalla el conjunto resultante.'''

numeros = set()
numeros.add(1)
numeros.add(2)
numeros.add(3)
numeros.add(4)
numeros.add(5)
print(numeros)

print("Ejercicio0 N4")
'''Crea un conjunto llamado "vocales" que
contenga las vocales del alfabeto.
Pide al usuario que ingrese una letra y verifica si
esa letra está presente en el conjunto "vocales".
Muestra un mensaje en pantalla indicando si la
letra es una vocal o no.'''

vocales = {"a","e","i","o","u"}
letra = input('Ingrese una letra: ')
if letra in vocales:
    print(letra," está en el conjunto")
else:
    print(letra," no esta en el conjunto")

print("ejercicio N°5")
'''Crea una lista llamada "numeros_repetidos" que
contenga números repetidos.
Convierte la lista en un conjunto utilizando la
función set() para eliminar los elementos
duplicados.
Convierte el conjunto resultante nuevamente en
una lista y muéstrala en pantalla.'''

numeros_repetidos = [2,4,6,2,4,4,5]
set = set(numeros_repetidos)
print("conjunto sin repeticiones: ",set)

print("ejrcicio N°6")
'''Crea dos conjuntos: "set1" con los números del 1
al 5, y "set2" con los números del 4 al 8.
Utiliza los métodos de conjuntos para realizar las
siguientes operaciones e imprime los resultados:
Obtener la diferencia simétrica entre set1 y set2.
Comprobar si set1 es un subconjunto de set2.
Comprobar si set2 es un subconjunto propio de
set1.'''

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
#diferencia simétrica
difference = set1.symmetric_difference(set2)
print(difference)
print("----")
#comprobacion de subconjuntos
is_subset = set1.issubset(set2)
print(is_subset)
print("----")
#subconjunto propio
is_proper_subset = set2.issubset(set1) and set2 != set1
print(is_proper_subset)

print("Ejercicio N°7")
'''Crea dos conjuntos llamados "set_a" y "set_b"
con elementos en común.
Utiliza un método de conjuntos para eliminar los
elementos comunes de set_a en relación con
set_b.
Imprime en pantalla el conjunto resultante de
set_a.'''

set_a = {"gato","perro","paloma","tortuga"}
set_b = {"gato","perro"}
set_a = set_a - set_b
print("Conjunto resultante eliminando los elementos iguales: ",set_a)

