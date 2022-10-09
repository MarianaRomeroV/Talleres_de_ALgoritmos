import math
#Entradas
Parcial_uno=float(input("Digite nota del parcial uno"))
Parical_dos=float(input("Digite nota del parcial dos"))
Parical_tres=float(input("Digite nota del parcial tres"))
Examen=float(input("Ingrese nota del examen"))
Trabajo=float(input("Digite nota del trabajo final"))
#Caja negra 
calificacion_final=(((Parcial_uno+Parical_dos+Parical_tres)/3)*0.55+(Examen*0.3)+(Trabajo*0.15))
#Salida
print("La nota final es:" +str(calificacion_final))