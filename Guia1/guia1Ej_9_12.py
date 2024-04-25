#%%
#Ingresar por teclado usuario y contraseña. Debe indicar si el usuario ingresado es
#correcto o no.

print("***EJERCICIO N° 9***")
print("")
usuario="milena"
contrasena="1234di"

us=input('Ingrese usuario: ')
cn=input('Ingrese contraseña: ')

if usuario==us and contrasena==cn:
    print("Usuario correcto")
else:
    print("Usuario o contraseña incorrecto")

#%%
#Realizar un programa que solicite números y finalice al ingresar un valor 0. Al
#terminar indicar la sumatoria total.
print("***EJERCICIO N°10***")
print("")

valor=int(input('Ingrese un valor'))
suma=0

while valor!=0:
    suma=suma+valor
    valor=int(input('Ingrese un valor'))

print(f"la sumatoria total es {suma}")


# %%
#11) Realizá un programa que permita ingresar el monto mensual de ventas realizadas
#por un comercio durante el año (un ingreso por mes). A su vez ingresar gasto por
#mes. Calcular:
#a) Facturación anual
#b) Ganancia mensual
#c) Ganancia promedio

print('***EJERCICIO N° 11***')

facturacion_anual=0
suma_ganancia=0
meses=int(input('ingrese cantidad de meses: '))
for i in range (meses):
    monto_mensual=int(input('Ingrese monto del mes'))
    gasto_mensual=int(input('gasto mensual'))
    facturacion_anual=facturacion_anual+(monto_mensual-gasto_mensual)
    ganancia_mensual=monto_mensual-gasto_mensual
    print(f'Ganancia mensual del mes {i+1}: {ganancia_mensual}')
    suma_ganancia=suma_ganancia+ganancia_mensual
    ganancia_promedio=suma_ganancia/meses

print(f'Facturacion anual: {facturacion_anual}')
print(f'Ganancia Promedio: {ganancia_promedio} % por mes')

# %%
#12) Realizar una calculadora que permita ingresar dos valores y la operación a realizar y
#brinde el resultado en pantalla. El programa no finaliza.

print("***EJERCICIO N°12***")
#true=true

while True:
    print("")
    print("*****************")
    print("")
    print("A - SUMA")
    print("B - RESTA")
    print("C - MULTIPLICACIÓN")
    print("D - DIVISIÓN")
    print("E - SALIDA")
    print("")
    
    opcion= input('Ingrese la opcion a calcular')
    if opcion=='E':
        print("GRACIAS POR USAR NUESTRO SISTEMA")
        break
    valor1=int(input('Ingrese el primer valor'))
    valor2=int(input('Ingrese el segundo  valor'))
    
    if opcion=='A':
        suma=valor1+valor2
        print(f"La suma es: {suma}")
    elif opcion=='B':
        resta=valor1-valor2
        print(f"La resta es: {resta}")
    elif opcion=='C':
        multip=valor1*valor2
        print(f"La Multiplicacion es: {multip}")
    elif opcion=='D':
        div=valor1//valor2
        print(f"La division es: {div}")
    

# %%
