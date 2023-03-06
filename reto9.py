#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40  

lista = [numero for numero in (50,45,20,30,40,87) if numero > 40]
print(lista)