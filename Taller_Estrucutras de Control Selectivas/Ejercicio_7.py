#entrada
Km=float(input("Digite distancia recorrida:"))
#caja negra
if (Km<=300):
    print("Se deben pagar 50.000 ")  
elif(Km>300) and (Km<=1000):
    total=(Km-300)*30000+70000
    print(" El total a pagar es de: "+str(total))
elif(Km>1000):
    total=(Km-300)*9000+150000
    print("El total a pagar es de: "+str(total))