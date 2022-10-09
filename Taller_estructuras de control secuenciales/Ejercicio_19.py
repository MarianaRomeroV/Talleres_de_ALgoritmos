#Entradas
Cantidad_naranjas=int(input("Digite la cantidad de naranjas compradas: "))
Precio=int(input("Digite el precio por una docena de naranjas: "))
Venta=int(input("Digite el precio de venta de las naranjas: "))
#Caja negra
Inversión=(Cantidad_naranjas*Precio)/12
Naranjas=(Venta-Inversión)*100/Inversión
#Salida
print("El porcentaje de ganancia en la inversion es:",Naranjas)