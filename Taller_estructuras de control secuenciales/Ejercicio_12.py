#Entradas
Matematicas=(float(input("ingrese nota de examen matematicas: ")))
Física=(float(input("ingrese nota examen fisica: ")))
Química=(float(input("ingrese nota examen quimica: ")))
M1=float(input("ingrese nota de la tarea uno Matemáticas: " ))
M2=float(input("ingrese nota de la tarea dos Matemáticas: " ))
M3=float(input("ingrese nota de la tarea tres Matemáticas: " ))
F1=float(input("ingrese nota de la tarea uno Física: " ))
F2=float(input("ingrese nota de la tarea dos Física: " ))
Q1=float(input("ingrese nota de la tarea uno Química: " ))
Q2=float(input("ingrese nota de la tarea dos Química: " ))
Q3=float(input("ingrese nota de la tarea tres Química: " ))
#Caja negra
Promedio_Math=((Matematicas*0.90)+(((M1+M2+M3)/3)*0.10))
Promedio_Física=((Física*0.80)+((F1+F2)/2)*0.20)
Promedio_Química=((Química*0.85)+(((Q1+Q2+Q3)/3)*0.15))
Promedio_Final=(Promedio_Math+Promedio_Física+Promedio_Química)/3
#Salidas
print(("Promedio de Matemáticas es:", Promedio_Math))
print(("Promedio de Física es:", Promedio_Física))
print(("Promedio de Química es:", Promedio_Química))
print(("El promedio general del semestre es:", Promedio_Final))