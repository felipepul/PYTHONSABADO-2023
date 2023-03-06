#Recibir un numero en teclado y determinar si este es múltiplo de 3
print("Digite elnumero  para determinar si es multiplo de 3")
print ("")
numero = int(input("digite el numero a determinar: "))
result = numero %  3
if (result == 0):
    print(f"el numero {numero} si es multiplo de 3")
else:
    print(f"el numero {numero} no es multiplo de 3")