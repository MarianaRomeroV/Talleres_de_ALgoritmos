#entradas
Capital=float(input("Digite el capital a invertir: "))
Interés=float(input("Digite la tasa de interes %:  "))
#caja negra
if(Capital>100000):
   Ganancia=(Capital*Interés)
#salidas
print("La ganancia será de: " +str(Ganancia))
Ganancia_1=Capital+Ganancia
print("El dinero total que está en la cuenta es de: " +str(Ganancia_1))