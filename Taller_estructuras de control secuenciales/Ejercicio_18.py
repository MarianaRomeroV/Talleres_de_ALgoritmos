#Entradas
Cantidad_Bolivares=int(input("Ingrese la cantidad del prestamo de Bolívares: "))
Interes=int(input("Ingrese la cantidad de interes en 4 años: "))
#Caja negra
BolivaresX=(Interes*100)/(Cantidad_Bolivares*4)
Porcentaje=BolivaresX/4
#Salida
print("El porcentaje anual cobrado por el prestamo es de: ", Porcentaje)