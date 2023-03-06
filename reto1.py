#Recibir un numero en teclado y determinar si este es múltiplo de 5
numeroIngreso = int(input("Digite un numero, para validar: "))
numero = int(input("Digite un numero: "))
result = numero % numeroIngreso
if (result == 0):
    print(f"el numero {numero} si es multiplo de {numeroIngreso}")
else:
    print(f"el numero {numero} no es multiplo de {numeroIngreso}")

