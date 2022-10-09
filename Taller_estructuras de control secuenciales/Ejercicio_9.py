#Entradas 
Horas_trabajadas=float(input("Ingrese numero de horas trabajas: "))
Precio_hora=float(input("Ingre el precio de la hora: "))
#Caja negra
Sueldo_base=(Horas_trabajadas*Precio_hora)
Salario_neto=(Sueldo_base)-(Sueldo_base*0.20)
#Salidas
print("El salario neto del trabajador es:", Salario_neto)
