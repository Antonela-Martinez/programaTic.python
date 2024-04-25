#Este es un comentario simple
'''comentario de varias lineas
Aca evaluamos un valor con if
ctl+shift+7 comenta lo seleccionado
* Variables primitivas: int,float, string, boolean
* fincion de lectura por teclado -> INPUT
* Funcion de escritura por teclado -> PRINT
* Funcion de Chequeo de tipo de dato -> type 
* PYTHON no necesita tipado de dato. Los infiere
*ejemplo de creacion de variable: variable= "texto de prueba" 
*OPERADORES DE ASIGNACION: =
*OPERADORES ARITMETICOS= += -= /= *=
*OPERADORES DE COMPARACION: == '''
#%%
#variable1=5
#print("el numero es" + variable1) '''Me da error xq hay un int y solo muestra por pantalla string'''

#print("hol" + str(variable2))// conv string
#print("hol" + {variable2}) //para convertir a string
#print(f"el numero es{num1}")   ##f es para formatear para pasar a string

#variable = input("ingrese un numero")
#sprint("El numero es" + variable)

#ESTRUCTURA DE DESICION
#input lee el dato por teclado y lo guarda en una variable(me loguarda como un string)
#int-> para convertir el dato ingresado a entero
num=int(input("ingresar un numero")) 

if num<10:
    print("el numero es menor")
else:
    print("es mayor ")

print(type(num)) #Me dice de que tipo es la variable
#%%
#ESTRUCTURA REPETITIVA
#(for)
sumatoria=0
for i in range(0,5): #reiny
    num=int(input("ingrese un valor: "))
    sumatoria+=num
print(f"la suma es{sumatoria}")

#(while)Hasta que condicion se cimpla se repite
tope=20
num=int(input('ingreseun valor: '))
while num<tope:
    num=int(input('ingrese un valor'))

print(f"Salio.valor ingresado{num}")