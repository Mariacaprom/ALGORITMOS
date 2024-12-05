#calcular un salario
salario_bruto =float(input("Ingrese el salario bruto: "))
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuestos (%): "))
impuesto = (salario_bruto * porcentaje_impuesto) / 100
salario_neto = salario_bruto - impuesto
print (f"El impuesto es: ${impuesto:.2f}")
print (f"El salario neto es:. ${salario_neto:.2f}")

