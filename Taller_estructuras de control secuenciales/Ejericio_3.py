#Entradas
Dinero_base=int(input("Ingrese su sueldo base:"))
Venta_1=int(input("Digite venta uno:"))
Venta_dos=int(input("Digite venta dos:"))
Venta_tres=int(input("Digite venta tres:"))
#Caja negra
Comision=((Venta_1+Venta_dos+Venta_tres)*0.1)
Sueldo_total=(Dinero_base+Comision)
#Salidas
print("El valor del sueldo total del mes es: ", Sueldo_total)
print("El valor de las comisiones es:" , Comision)
