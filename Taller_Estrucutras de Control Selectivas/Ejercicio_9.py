#Entradas
Nombre=input("Digite su nombre: ")
Monto_Producto=float(input("Digite el valor del producto: "))
#caja negra
if (Monto_Producto<50000):
  d=0
  print("No es posible realizar el descuento", Nombre)
elif(Monto_Producto>=50000 and Monto_Producto<=100000):
  descuento=Monto_Producto*0.5
  print ("El descuento aplicado será del 5% ")
elif(Monto_Producto>=100000 and Monto_Producto<=700000):
  descuento=Monto_Producto*0.11
  print("El descuento aplicado será del 11% ")
elif(Monto_Producto>=700000 and Monto_Producto<=1500000):
  descuento=Monto_Producto*0.18
  print("El descuento aplicado será del 18%")
elif(Monto_Producto>=1500000):
    descuento=Monto_Producto*0.25
    print("El descuento aplicado será del 25% ")
#Salidas
print("Cliente", Nombre,)
print("El costo final del producto es: ", (Monto_Producto))
print("El precio final será de:", (Monto_Producto-descuento))
