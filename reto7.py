#Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario

lista = []
tamano_lista = int(input("Ingrese el tamaño de la lista: "))
for i in range(tamano_lista): 
    numero = int(input("Ingrese un número: ")) 
    lista.append(numero) 
print("La lista creada es: ",lista)