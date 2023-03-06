#Construir un programa que reciba números enteros y los sume mientras estos sean positivos, si se digita un número negativo el programa debe terminar

suma = 0
numero = int(input("Ingrese un número entero: "))
while numero > 0: 
    suma += numero 
    numero = int(input("Ingrese otro número entero: ")) 
print("La suma de los números ingresados es:",suma)