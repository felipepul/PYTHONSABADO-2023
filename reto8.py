#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES

lista_pares=[x for x in (50,45,20,30,40,87) if x % 2==0]
print(lista_pares)