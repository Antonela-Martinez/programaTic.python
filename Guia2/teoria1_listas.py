#ESTRUCTURA DE DATOS
#listas
#Duplas
#set
#diccionario

#DECLARO UNA VARIABLE(lista)
variable=[]
list=["hola", "chau", 123, True] #Podes agrupar cualquier valo ren una lista. Mass flexible
                                #le puedo ir agregando valoares

#%%
#LISTAS
lista_frutas=["fresa", "uva", "cereza","sandia","Melon"]
lista_frutas[1]="Frambuesa" #Reeplazo por este dato en esta posicion
print(lista_frutas)
print(lista_frutas[1])
print(lista_frutas[1:3])
#%%
#RECORRO LA LISTA Y ME LO MUESTRA
lista_frutas=["fresa", "uva", "cereza"]
#----------RECORRO con for
for x in lista_frutas:
    print(x)
#---------Verifico si "fresa esta en la lista"
if "fresa" in lista_frutas:
    print("si, 'fresa' se encientra en la lista")

#-----------Cuantos valores tengo, LEN me dice el tamaño
print(len(lista_frutas))

#%%
#-----------RECORRO con while
nueva_lista=[1,2,3,4,5,6,7,8]
largo_lista= len(nueva_lista)
indice=0

while indice < largo_lista:
    print(nueva_lista[indice])
    indice += 1

#%%
#AÑADIR ELEMENTO
#-------Añade un elemento al final
lista_frutas=["fresa", "uva", "cereza"]
lista_frutas.append("mango")
print(lista_frutas)

# %%
#-------Añade un elemento en el index 1(antes del indice 1)
lista_frutas=["fresa", "uva", "cereza"]
lista_frutas.insert(1,"naranja")
print(lista_frutas)

# %%
#ELEMINAR
#---------EElimino elemento
lista_frutas=["fresa", "uva", "cereza"]
lista_frutas.remove("uva")
print(lista_frutas)

#-------Elimino elemento por indice y me devuelve ese valor
valor_eliminado= lista_frutas.pop()
print(lista_frutas)
print(f"valor eliminado: {valor_eliminado}")

# %%
lista_frutas=["fresa", "uva", "cereza"]
valor_eliminado= lista_frutas.pop(0)
print(lista_frutas)
print(f"valor eliminado: {valor_eliminado}")

# %%
#----------Elimino elemento puntual
lista_frutas=["fresa", "uva", "cereza"]
del lista_frutas[1]
print(lista_frutas)

#-------Limpiar lista completa
lista_frutas.clear()
print(lista_frutas)
# %%
#COPIA
#Quiero hacer una copia
lista_frutas=["fresa", "uva", "cereza"]
lista2=lista_frutas.copy()
print(lista2)
# %%
#Me hago una lista con el contenido de la lista
lista_frutas=["fresa", "uva", "cereza"]
lista3= list(lista_frutas)
print(lista_frutas)
# %%
#CONCATENACION DE LISTAS
#------Uso operador matematico
lista1=["a","b","c"]
lista2=[1,2,3]
print("Soy lista 1:",lista1)
print("Sooy lista 2:",lista2)
lista3= lista1 + lista2
print("Soy lista 3:",lista3)

#------Recorro lista2 y agrego lista1 al final
for x in lista2:
    lista1.append(x)
print("soy lista 1: ",lista1)

#---------Proceso de extencion(fusiona los contenidos, entiende quequiero el contenido)
lista1.extend(lista2)
print("Soy lista 1, use contenido de lista 2:",lista1)

#-----------APPEND > Loque vos me das metelo al fonto
lista1.append(lista2)
print("Soy lista 1: <APPEND> lo que vos me das ponelo al final:",lista1)
#lista1. (me da los medodos pr default)
# %%

