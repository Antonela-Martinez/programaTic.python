#Ingresar 10 valores, indicar para cada uno su paridad, y al final indicar cuántos pares
#y cuantos impares hubo.
#%%
print("***EJERCICIO N°5***")
print("")
par=0
impar=0

for i in range (5):
    num=int(input('Ingrese un valor: '))
    if num%2==0:
        print("Su numero es PAR")
        par=par+1
        print("")
    else:
        print("Su numero es IMPAR")
        impar=impar+1
        print("")

print(f"Cantidad de numeros PARES: {par} y cantidad de numero IMPARES: {impar}")
print("")

#%%
#Generalizar el punto anterior para ingresar N valores, indicar de cada uno su
#paridad, y al final indicar cuántos pares y cuantos impares hubo

print("***EJERCICIO N°6***")
print("")
par=0
impar=0

num=int(input('Ingrese un valor distinto de cero: '))

while (num!=0):
    if num%2==0:
        print(f"El numero {num} es PAR")
        par=par+1
        print("")
    else:
        print(f"El numero {num} es IMPAR")
        impar=impar+1
        print("")
        
    num=int(input('Ingrese un valor distinto de cero: '))

print(f"Cantidad de numeros PARES: {par} y cantidad de numero IMPARES: {impar}")
print("")

# %%
#Ingresar 10 valores por teclado. Indicar cuál fue el mayor y cuál fue el menor.

print("***EJERCICIO N° 7***")
print("")

max=1
min=10

for i in range (5):
    num=int(input('Ingrese un numero: '))
    if num>=max:
        max=num
    elif num<=min:
        min=num
 

print(f'El valor maximo es: {max} y el valor minimo es: {min}')
# %%
#Indicar por teclado cuántos números deben ingresarse, ingresarlos y luego calcular
#la suma o multiplicación de los mismos
print("***EJERCICIO N° 8***")
print("")

cantidad=int(input('Ingrese cantidad de valores a ingresar: '))
suma=0
multiplicacion=1
i=0

while i<cantidad:
    valor=int(input('Ingrese valor'))
    suma=suma+valor
    multiplicacion=multiplicacion*valor
    i=i+1
print(f'La suma es: {suma}')
print(f'la Multiplicacion es: {multiplicacion}')
# %%
