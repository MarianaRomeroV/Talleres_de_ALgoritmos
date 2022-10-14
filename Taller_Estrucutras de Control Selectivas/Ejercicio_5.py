#entradas
Salario_bruto=int(input("Digite salario: "))
Ventas_dp1=int(input("Digite ventas totales del departamento 1: "))
Ventas_dp2=int(input("Digite ventas totales del departamento 2: "))
Ventas_dp3=int(input("Digite ventas totales del departamento 3: "))
#caja negra
Venta_total=(Ventas_dp1+Ventas_dp2+Ventas_dp3)
print("Venta total: "+str(Venta_total))
Importe_global=(Venta_total*33)/100
if(Ventas_dp1>Importe_global):
    Ventas_dp1=Salario_bruto+Salario_bruto*.20
else:
    Ventas_dp1=Salario_bruto
print("Los vendedores del departamento 1 recibirán: "+str(Ventas_dp1))      
if(Ventas_dp2>Importe_global):
    Ventas_dp2=Salario_bruto+Salario_bruto*.20
else:
    Ventas_dp2=Salario_bruto 
print("Los vendedores del departamento 2 recibirán: "+str(Ventas_dp2))    
if(Ventas_dp3>Importe_global):
    Ventas_dp3=Salario_bruto+Salario_bruto*.20
else:
    Ventas_dp3=Salario_bruto      
print("Los vendedores del departamento 3 recibirán: "+str(Ventas_dp3))  