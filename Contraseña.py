# Algoritmo que valide contraseñas
contraseña = input("Ingrese su contraseña:")
if len(contraseña) >= 8:
    if any(char.isupper() for char in contraseña) and any(char.isdigit() for char in contraseña):
        print("La contraseña es valida")
    else:
        print("La contraseña debe contener al menos una letra mayuscula y un numero.")
else:
        print("La contraseña debe conener al menos 8 caracteres")
        