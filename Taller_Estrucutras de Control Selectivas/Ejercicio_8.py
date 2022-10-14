#entradas
P=int(input("Digite el valor del entero P: "))
Q=int(input("Digite el valor del entero Q: "))
#caja negra
Expresión=(P**3+Q**4-2*P**2)
if (Expresión<=680):
   print("P y Q satisfacen la expresión: "+str(Expresión)) 
elif(Expresión>=680):
   print("P y Q no satisfacen la expresión:")