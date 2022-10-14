#entrada
lectura_actual=int(input("Ingrese el valor de la lectura actual: "))
lectura_anterior=int(input("Ingrese el valor de la lectura anterior: "))
#Caja negra
Diferencia=abs(lectura_anterior - lectura_actual)
if (Diferencia>= 0 and Diferencia <= 100):
    costo = 4600
elif (Diferencia >= 101 and Diferencia <= 300):
    costo = 80000
elif (Diferencia >= 301 and Diferencia <= 500):
    costo = 100000
elif (Diferencia >= 501):
    costo = 120000
costo_final=(Diferencia*costo)
#Salidas
print("El precio segun la tabla de Kwh es de:", round(costo))
print("El total que debe pagar de luz eléctrica y servicio de aseo es de:", round(costo_final))