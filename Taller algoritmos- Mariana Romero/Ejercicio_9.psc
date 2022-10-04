Algoritmo Vendedor_sueldo_comisión
	//entradas
	Escribir "Digite su sueldo base"
	Leer sueldo_base
	Escribir "Digite el valor de la venta 1"
	Leer Venta_1
	Escribir "Digite el valor de la venta 2"
	Leer Venta_2
	Escribir "Digite el valor de la venta 3"
	Leer Venta_3
	//caja negra
	comision_por_venta<-(Venta_1+Venta_2+Venta_3)*0.10
	suledo_total<-sueldo_base+comision_por_venta
	//salidas
	Escribir "El dinero recibido por comisiones totales es: "  comision_por_venta
	Escribir "El sueldo total del mes es:  "  sueldo_base
FinAlgoritmo
