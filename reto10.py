# Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso

lista = []
for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    lista.append(numero)
numero_buscar = int(input("Ingrese el número a buscar: "))
if numero_buscar in lista:  
    print(f"El resultado es exitoso numero buscado es el: {numero_buscar} y esta en la lista") 
else: 
    print(f"El numero buscado es el:{numero_buscar} y no se encuentra") 