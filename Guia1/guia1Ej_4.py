#Realizá un programa que permita resolver el siguiente problema: Cuatro personas
#aportan diferente capital a una sociedad y desean saber el valor total aportado y qué
#porcentaje aportó cada una (indicando nombre y porcentaje).
#Solicitar la carga por teclado del nombre de cada socio, su capital aportado y a partir
#de esto calcular e informar lo requerido previamente.

persona1_nombre=input("Ingrese su nombre persona 1: ")
persona1_capital=int(input("Ingrese capital persona 1: "))
persona2_nombre=input("Ingrese su nombre Persona 2: ")
persona2_capital=int(input("Ingrese capital persona 2: "))
persona3_nombre=input("Ingrese su nombre persona 3: ")
persona3_capital=int(input("Ingrese capital persona 3: "))
persona4_nombre=input("Ingrese su nombre persona 4: ")
persona4_capital=int(input("Ingrese capital persona 4:"))

total=persona1_capital+persona2_capital+persona3_capital+persona4_capital

porcentaje_p1=(persona1_capital*100)/total
porcentaje_p2=(persona2_capital*100)/total
porcentaje_p3=(persona3_capital*100)/total
porcentaje_p4=(persona4_capital*100)/total

print(f"El capital total es: {total}")
print(f"El porcentaje aportado por {persona1_nombre} es: {porcentaje_p1} %")
print(f"El porcentaje aportado por {persona2_nombre} es: {porcentaje_p2} %")
print(f"El porcentaje aportado por {persona3_nombre} es: {porcentaje_p3} %")
print(f"El porcentaje aportado por {persona4_nombre} es: {porcentaje_p4} %")