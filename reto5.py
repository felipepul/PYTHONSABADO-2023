#Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7

lista = []
tamano = int(input("Ingrese el tamaño de la lista: "))
for i in range(tamano): 
    lista.append(7*i)
    print(lista)