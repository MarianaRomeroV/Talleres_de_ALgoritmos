#Entradas
Estudiantes=int(input("Numero total de estudiantes: "))
Hombres=int(input("Numero de hombres en el grupo: "))
Mujeres=int(input("Numero de mujeres en el grupo: "))
#Caja negra
porcentaje_hombres=((Hombres/Estudiantes)*100)
porcentaje_mujeres=((Mujeres/Estudiantes)*100)
#Salidas
print("El porcentaje de hombres en el grupo es:", porcentaje_hombres)
print("El porcentaje de mujeres en el grupo es:", porcentaje_mujeres)