Algoritmo Calificaci�n_materia_algoritmos
	//entrada
	Escribir "Digite calificacion_parcial1: "
	Leer Calificaci�n_parcial1
	Escribir "Digite Calificaci�n_parcial2:  "
	Leer Calificaci�n_parcial2
	Escribir "Digite Calificaci�n_parcial3:  "
	Leer Calificaci�n_parcial3
	Escribir "Digite Calificaci�n_examen:  "
	Leer Calificaci�n_examen 
	Escribir "Digite Calificaci�n_trabajo:  "
	Leer Calificaci�n_trabajo
	//caja negra
	Calificaci�n_parcial<-((Calificaci�n_parcial1+Calificaci�n_parcial2+Calificaci�n_parcial3)/3)*0.55
	Calificaci�n_examen<-Calificaci�n_examen*0.3
	Calificaci�n_trabajo<-Calificaci�n_trabajo*0.15
	Calificaci�n_final<-Calificaci�n_parcial+Calificaci�n_examen+Calificaci�n_trabajo
	//salidas
	Escribir Calificaci�n_parcial
	Escribir Calificaci�n_examen
	Escribir Calificaci�n_trabajo
	Escribir "Su nota final es:  " Calificaci�n_final
FinAlgoritmo
