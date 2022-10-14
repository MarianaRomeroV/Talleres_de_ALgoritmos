#entradas
Salario=int(input("Digite su salario:") ) 
Categoria=int(input("Digite su categoria del 1 al 5: ")) 
#caja negra
if (Categoria==1):
  a=Salario*0.1
if (Categoria==2): 
  a=Salario*0.15 
if (Categoria==3):
  a=Salario*0.20
if (Categoria==4): 
  a=Salario*0.40
if (Categoria==5): 
  a=Salario*0.60 
Salario_neto=Salario+a
#salidas 
print("El aumento sera de: "+str(a))
print("Valor del sueldo nuevo: " +str(Salario_neto))