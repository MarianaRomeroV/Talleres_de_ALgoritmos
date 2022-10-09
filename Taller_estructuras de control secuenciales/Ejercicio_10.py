#Entradas
Chelines=int(input("Ingrese la cantidad de chelines austriacos: "))
Dracmas=int(input("Ingrese la cantidad de dracmas griegos: "))
Pesetas=int(input("Ingrese la cantidad de pesetas: "))
#Caja negra
Chelin_Peseta=(Chelines*956.871)/100
Dracma_Franco=((Dracmas*88.607)/100)/20.110
Peseta_Dolar=Pesetas/122.499
Peseta_liria=Pesetas*100/9.289
#Salidas
print("El equivalente de chelines a pesetas es:", Chelin_Peseta) 
print("El equivalente de dracmas griegos a francos es:", Dracma_Franco) 
print("El equivalente de pesetas a dolares es:",Peseta_Dolar) 
print("El equivalente de pesetas a liras italianas es:",Peseta_liria) 