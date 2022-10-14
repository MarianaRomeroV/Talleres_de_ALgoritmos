#Entradas
print("Ingrese: Años, Meses, SEXO(F o M), NIVEL DE HEMOGLOBINA (sin unidad): ")
print("EJEMPLO: 10 0 F 16")
datos = input()
lista_datos = datos.split(" ")
año= int(lista_datos[0])
meses=int(lista_datos[1])
#Caja negra
if (meses == 12 and año== 0) or (meses == 0 and año== 1):
    año = 1
    meses =12
sexo = lista_datos[2].capitalize()
nivel_hemoglobina = float(lista_datos[3])
if ((meses >= 0) and (meses <=1)):
    if (nivel_hemoglobina >= 13 and nivel_hemoglobina <= 26):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (meses > 1 and meses <= 6):
    if (nivel_hemoglobina >= 10 and nivel_hemoglobina <= 18):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (meses > 6 and meses <= 12):
    if (nivel_hemoglobina >= 11 and nivel_hemoglobina <= 15):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (año > 1 and año <= 5):
    if (nivel_hemoglobina >= 11.5 and nivel_hemoglobina <= 15):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (año > 5 and año <= 10):
    if (nivel_hemoglobina >= 12.6 and nivel_hemoglobina <= 15.5):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (año > 10 and año <= 15):
    if (nivel_hemoglobina >= 13 and nivel_hemoglobina <= 15.5):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (año > 15 and sexo == "M"):
    if (nivel_hemoglobina >= 12 and nivel_hemoglobina <= 16):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")
elif (año > 15 and sexo == "M"):
    if (nivel_hemoglobina >= 13 and nivel_hemoglobina <= 26):
        print("Resultado NEGATIVO PARA ANEMIA")
    else:
        print("Restultado POSITIVO PARA ANEMIA")