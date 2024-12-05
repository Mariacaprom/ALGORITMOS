# Calcular el precio de descuento
precio_original =float(input("Ingrese el precio original del producto: "))
porcentaje_descuento =float(input("Ingrese el porcentaje de descuento: "))
if precio_original >= 100:
    descuento = (precio_original * porcentaje_descuento) / 100
    precio_final = precio_original - descuento
    print(f"El descuento es: ${descuento:.2f}")
    print(f"El precio final es: ${precio_final:.2f}")
else:
    print(f"No se aplica descuento. El precio final es: ${precio_original:.2f}")
    