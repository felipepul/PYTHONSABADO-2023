#Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados
ciudadesColombianas = []
tamano = 8
for i in range(tamano):
    ciudadesColombianas.append(input(f"Digite una ciudad colombiana para la posicion {i+1}: "))
ciudadesColombianas.reverse()
print(ciudadesColombianas)