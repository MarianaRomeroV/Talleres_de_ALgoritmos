#Entradas
Lectura_anterior=int(input("Ingrese lectura antigua: "))
Lectura_actual=int(input("Ingrese lectura actual: "))
Costo_Kw=int(input("Ingrese costo por kilovatio: "))
#Caja negra
Monto_total=Lectura_actual*Costo_Kw
#Salidas
print("El monto total a pagar es de:", Monto_total)