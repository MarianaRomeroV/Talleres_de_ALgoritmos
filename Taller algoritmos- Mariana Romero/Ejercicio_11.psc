Algoritmo Calificación_materia_algoritmos
	//entrada
	Escribir "Digite calificacion_parcial1: "
	Leer Calificación_parcial1
	Escribir "Digite Calificación_parcial2:  "
	Leer Calificación_parcial2
	Escribir "Digite Calificación_parcial3:  "
	Leer Calificación_parcial3
	Escribir "Digite Calificación_examen:  "
	Leer Calificación_examen 
	Escribir "Digite Calificación_trabajo:  "
	Leer Calificación_trabajo
	//caja negra
	Calificación_parcial<-((Calificación_parcial1+Calificación_parcial2+Calificación_parcial3)/3)*0.55
	Calificación_examen<-Calificación_examen*0.3
	Calificación_trabajo<-Calificación_trabajo*0.15
	Calificación_final<-Calificación_parcial+Calificación_examen+Calificación_trabajo
	//salidas
	Escribir Calificación_parcial
	Escribir Calificación_examen
	Escribir Calificación_trabajo
	Escribir "Su nota final es:  " Calificación_final
FinAlgoritmo
