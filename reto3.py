#Recibir dos números y determinar cual es mayor
valorUno = int(input("Digite el  numero uno "))
valorDos = int(input("Digite el  numero dos "))
if(valorUno > valorDos):
    print(f"el numero{valorUno} es mayor")
elif(valorDos >valorUno):
    print(f"el numero {valorDos} es mayor")
else:
    print(f" el  {valorUno} y el  {valorDos} son iguales")


'''import random
tamano = 5
numeros = [random.randint (0, 10) for i in range(tamano)]
buscarNumero = int(input('Digite un numero a buscar: '))
validar = False
for i in range(tamano):
    if numeros[i] == buscarNumero:
        validar = True
        break
if validar == True:
    print(f'Numero buscado se encuentra en la lista: {buscarNumero}')
    print(numeros)
else:
    print(f'Numero buscado no se encuentra en la lista: {buscarNumero}')
    print(numeros)'''








