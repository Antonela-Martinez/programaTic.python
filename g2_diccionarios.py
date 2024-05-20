'''Ejercicio N° 1
Crea un diccionario llamado "alumno" que
contenga las siguientes claves: "nombre",
"edad" y "carrera". Asigna valores adecuados a
cada clave.
Imprime en pantalla la información del alumno
utilizando las claves del diccionario.'''

alumno = {
    "Nombre": "Laura",
    "Edad": 20,
    "Carrera": "Informática"
}
#print(alumno)

#Como hago para hacer con alumno.value o alumno.keys
#for x in alumno:
#    print(x,alumno[x])

x = alumno["Nombre"]
print(x)
x = alumno["Edad"]
print(x)
x = alumno["Carrera"]
print(x)

print("Ejercicio N° 2")
'''Modifica el valor de la clave "edad" en el
diccionario "alumno" y actualízalo con una
nueva edad.
Imprime en pantalla la información actualizada
del alumno.'''

alumno["Edad"] = 30
print(alumno)

print("Ejercicio N° 3")
'''Agrega una nueva entrada al diccionario
"alumno" con la clave "universidad" y un valor
correspondiente a la universidad en la que
estudia.
Imprime en pantalla la información completa del
alumno, incluyendo la nueva entrada.'''

alumno.update({"Universidad":"UTN"})
print(alumno)

print("Ejercicio N° 4")
'''
Crea un diccionario llamado "calificaciones" que
contenga las claves "matemáticas", "física" y
"química", y asigna valores numéricos a cada
una.
Utiliza un bucle para recorrer el diccionario e
imprimir en pantalla cada clave y su respectivo
valor.
'''
calificaciones = {
    "Matemáticas" : 5,
    "Física" : 7,
    "Química" : 9 
}
for x in calificaciones:
    print(x,calificaciones[x])

print("Ejercicio N° 5")
'''En base al ej 4:
Elimina la entrada correspondiente a la clave
"química" del diccionario "calificaciones".
Vuelve a recorrer el diccionario y muestra en
pantalla las claves y valores restantes.'''

calificaciones.pop("Química")
for x in calificaciones:
    print(x,calificaciones[x])

print("Ejercicio N° 6")
'''En base al ej 4:
Utiliza el método keys() para obtener una lista
de todas las claves del diccionario
"calificaciones".
Utiliza el método values() para obtener una lista
de todos los valores del diccionario.'''

calificaciones = {
    "Matemáticas" : 5,
    "Física" : 7,
    "Química" : 9 
}

list_keys = []
for x in calificaciones:
    list_keys.append(x)

print("las claves son: ",list_keys)

list_values = []
for x in calificaciones:
    list_values.append(calificaciones[x])

print("Los valores son: ",list_values)

#for x in calificaciones.values():
#    print(x,calificaciones[x])

print("Ejercicio N° 7")
'''Crea un diccionario llamado "agenda" que
contenga información de contactos.
Cada contacto debe ser representado por un
diccionario con claves como "nombre",
"teléfono" y "email".
Agrega al menos tres contactos al diccionario
"agenda" y muestra la información de cada
contacto en pantalla.'''

agenda = {
    "Contacto 1" : {"Nombre": "Vanesa", "Teléfono" : 2346789045, "Email" : "vane@gmail.com"},
    "Conntacto 2" : {"Nombre": "Clara", "Teléfono" : 2346789076, "Email" : "clara@gmail.com"},
    "Conntacto 3" : {"Nombre": "Mercedez", "Teléfono" : 2346889045, "Email" : "mer@gmail.com"},
    "Conntacto 4" : {"Nombre": "Sebastian", "Teléfono" : 2346767771, "Email" : "seba@gmail.com"}
}

for x, y in agenda.items():
    print(x,y)