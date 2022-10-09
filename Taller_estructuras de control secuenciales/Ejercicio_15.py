#Entradas
Precio_producto=float(input("Ingrese el precio final del producto: "))
Precio_venta=float(input("Ingrese el precio de venta al público del producto: "))
#Caja negra
P=(Precio_venta-Precio_producto)/Precio_producto
Descuento=P*100
#Salidas
print("El porcentaje de descuento que le ha sido aplicado es de:", Descuento)