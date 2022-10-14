#entradas
a=int(input("Digite el valor de a: "))
b=int(input("Digite el valor de b: "))
c=int(input("Digite el valor de c: ")) 
d=int(input("Digite el valor de d: "))
#caja negra
if (d==0) :
   e=(a-c)**2
   print("el valor de las expresiones serán de :" +str(e))
elif (d>0):
   e=(a-b)**2/d
print("el valor será de las expresiones serán de :" +str(e))