Nombre=[]
Porcentaje=[]
F=G=0
while True:
    N=input("Ingrese el nombre del estudiante: ")
    P=float(input("Ingrese el puntaje del estudiante: "))
    Nombre.append(N)
    Porcentaje.append(P)
    C=float(input("¿Desea continuar?\nDigite 0-SI y 1-NO "))
    if (C==1):
        break
for k in range((len(Porcentaje))):
    if (Porcentaje[k]<(sum(Porcentaje)/len(Porcentaje))):
            F+=1
    elif (Porcentaje[k]>(sum(Porcentaje)/len(Porcentaje))):
            G+=1
F=round((F*100)/len(Porcentaje),2)
G=round((G*100)/len(Porcentaje),2)
A=B=0
R=Porcentaje[0]
for i in range(len(Porcentaje)):
    if (Porcentaje[i]>R):
        R=Porcentaje[i]
        A=i
print("El estudiante con mayor puntaje es: ",Nombre[A])
for j in range(len(Porcentaje)):
    if (Porcentaje[j]<R):
        R=Porcentaje[j]
        B=j
print("El estudiante con menor puntaje es: ",Nombre[B])
print("El puntaje maximo obtenido es: ",max(Porcentaje))
print("El puntaje minimo obtenido es: ",min(Porcentaje))
print("El promedio de todos los puntajes es: ",round(sum(Porcentaje)/len(Porcentaje),2))
print(f"El porcentaje inferior al promedio fue de: {F}")
print(f"El porcenatje superior al promedio fue de: {G}")