#Entradas
Precio=float(input("Ingrese el precio de la computadora: "))
Recargo=float(input("Ingrese el interés de la compra por cada cuota: "))
#Caja negra
A=Precio/12
B=(A*Recargo)/100+A
C=(B-A)*100/A
#Salidas
print("El cobro en porcentaje por los intereses del computador es: ", C)
print("La cuota a pagar en conjunto al recargo mensual es:", B)
