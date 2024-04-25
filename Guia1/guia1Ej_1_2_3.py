#Ingresar un valor por teclado y avisar por consola si es positivo o negativo
num= int(input("Ingrese un numero"))

if num>0:
    print("su numero es positivo")
elif num<0:
    print("Su numero es negativo")
else:
    print("su numero es cero")

#%%
#Ingresar el radio de un círculo. Indicar en consola su perímetro y superficie.
radio= int(input("Ingrese el radio"))
pi=3.14

perimetro= 2*pi*radio
area=pi*radio*radio

print(f"El perimetro es: {perimetro} y el area es: {area}")


# %%
#Ingresar un valor por teclado y avisar por consola si es par o impar
print("***EJERCICIO N°3***")
print("")
num= int(input("Ingrese un numero"))

if num%2==0:
    print("su numero es PAR")
else:
    print("su numero es IMPAR")



# %%
