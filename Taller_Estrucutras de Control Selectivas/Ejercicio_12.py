#entradas
COP= int(input("Ingrese una cantidad entera de pesos colombianos (COP): "))
cop_str = str(COP)
billetes = [100_000, 50_000, 20_000, 10_000, 5_000, 2_000, 1_000, 500, 200, 100, 50]
nuevo_cop = 0
cantidad_unidad = [ 0 for i in range(11)]
#caja negra
for i in range(len(billetes)):
    if COP // billetes[i] > 0:
        cantidad_unidad[i] = (COP // billetes[i])
        COP= COP - (cantidad_unidad[i] * billetes[i] )
billetes_cantidades = zip(billetes, cantidad_unidad)
lista = list(billetes_cantidades)
lista_f_ceros = list((lista[i][0] * lista[i][1]) for i in range(11))
lista_f_no_ceros = list(dict.fromkeys(lista_f_ceros))
lista_f_no_ceros.remove(0)
#Salidas
print(*lista_f_no_ceros , sep = ",")
