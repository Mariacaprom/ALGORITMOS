# Comparar tres numero
num1 =float(input("Ingrese el primer numero:"))
num2 =float(input("Ingrese el segundo numero:"))
num3 =float(input("Ingrese el tercer numero:")) 
if num1 > num2 and num1 > num3:
    print(f"El numero mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El numero mayor es: {num2}")
else:
    print(f"El numero mayor es: {num3}")
    
    
