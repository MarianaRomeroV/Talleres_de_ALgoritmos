#entradas
Cantidad_piezas=int (input("Digite la cantidad de piezas a comprar: "))
Valor_pieza=int (input("Digite el valor por pieza: "))
Total=(Cantidad_piezas*Valor_pieza)
#caja negra
if (Total>5000000):
  Inversión=(Total*0.55)
  Banco=(Total*0.30)
  Credito_Fabricante=(Total*0.15)
  print("La inversion será de: ", round(Inversión))
  print("El préstamo del banco será de: ", round(Banco))
  print("El crédito a pagar al fabricante es: " +str(Credito_Fabricante))
else:
  Inversión=(Total*0.70)
  Banco=(0)
  Credito_Fabricante=(Total*0.30)
  print("La inversión será de: ", round(Inversión))
  print("El préstamo en el banco será de: " +str(Banco))
  print("El crédito a pagar al fabricante es: " +str(Credito_Fabricante))
Intereses_Fabricante=(Credito_Fabricante*0.20)
print("El interés por el crédito es de: " +str(Intereses_Fabricante))