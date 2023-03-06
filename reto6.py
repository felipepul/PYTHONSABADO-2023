#Codificar un programa que presente un menú de 4 opciones y reciba un numero natural  para realizar las siguientes operaciones:
#	0: Salida
#	1: Encuentre si el número es múltiplo de 2
#	2: Encuentre la raíz cuadrada del número
#  	3: Sume 100 al número ingresado
#	4: Eleve a la 2 el número ingresado

numero = 0
print("\nMenú de opciones:") 
print("1. Encuentre si el número es múltiplo de 2") 
print("2. Encuentre la raíz cuadrada del número") 
print("3. Sume 100 al número ingresado") 
print("4. Eleve a la 2 el número ingresado") 
print("0. Salida") 
opcion = int(input("Seleccione una opción: ")) 
if opcion == 0: 
    print("Saliendo...") 
elif opcion == 1: 
    numero = int(input("Ingrese un número: ")) 
    if numero % 2 == 0: 
        print(f"El número {numero} es múltiplo de 2") 
    else: 
        print(f"El número {numero} no es múltiplo de 2")  												  
elif opcion == 2: 
    numero = int(input("Ingrese un número: "))  
    raiz_cuadrada = numero ** (1/2)  
    print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")  			    
elif opcion == 3:  
    numero = int(input("Ingrese un número: "))  
    resultado = numero + 100  
    print(f"{numero} + 100 = {resultado}")  	    	    	    	    	    
elif opcion == 4:  
    numero = int(input("Ingrese un número: "))  
    resultado = numero ** 2  
    print(f"{numero} elevado a la 2 es igual a {resultado}")
else:
    opcion
    print(f"opcion incorrecta")