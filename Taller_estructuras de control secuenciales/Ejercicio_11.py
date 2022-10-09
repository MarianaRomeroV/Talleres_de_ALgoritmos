#Entradas
nombre=str(input("Ingrese el nombre del trabajador: "))
horas=float(input("Ingrese las horas trabajadas: "))
hora=float(input("Ingrese el pago por hora: "))
extras=int(input("Ingrese las horas extras trabajadas: "))
hijos=int(input("Ingrese el total de los hijos: "))
#Caja negra
Trabajdor=nombre
salario=horas*hora
Asignacion=(250000+173000*hijos+180000)
Deducciones=salario*(0.05+0.02+0.07)
Salario_descuentos=salario-Deducciones
A=horas*extras
B=A*0.25+A
Salario_neto=Asignacion+Deducciones+B
#Salidas
print("Las asignaciones son:", Asignacion)
print ("Las deducciones son:", Deducciones)
print("El salario neto que recibirá:", nombre)
print("en el mes de diciembre es de:", Salario_neto)