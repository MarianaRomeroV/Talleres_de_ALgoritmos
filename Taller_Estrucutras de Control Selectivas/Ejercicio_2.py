#entrada
Salario_bruto=float(input("Digite salario bruto: "))
#caja negra
if(Salario_bruto<900000):
  Sueldo_trabajador=Salario_bruto+(Salario_bruto*0.15)
  print("salario neto es igual: "+str(Sueldo_trabajador))
else:
  Sueldo_trabajador=Salario_bruto+(Salario_bruto*0.12)
  print("salario neto es igual: "+str(Sueldo_trabajador))