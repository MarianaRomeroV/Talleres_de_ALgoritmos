#entradas
from re import X

#Entradas
A=int(input("Digite el valor de la variable A: "))
B=int(input("Digite el valor de la variable B: "))
C=int(input("Digite el valor de la variable C: "))
D=int(input("Digite el valor de la variable D: "))
#caja negra
if (C>=5):
  X=A*1000
  Y=B*100
  N=X+(Y+100)
  print("El resultado redondeado es: ", (N))
else:
  X=A*1000
  sc=B*100
  N=X+(sc)
  print("El resultado redondeado es: ",(N))