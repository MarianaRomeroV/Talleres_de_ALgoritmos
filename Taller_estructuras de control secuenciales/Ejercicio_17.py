#Entrada
Presupuesto_hospital=float(input("Ingrese el presupuesto anual del Hospital:" ))
#Caja negra
Presupuesto_Gineco=Presupuesto_hospital*0.40
Presupuesto_Traumatología=Presupuesto_hospital*0.30
Presupuesto_Pediatría=Presupuesto_hospital*0.30
#Salidas
print("El presupuesto para el área de Ginecología es de: ", Presupuesto_Gineco)
print("El presupuesto para el área de Traumatología es de:", Presupuesto_Traumatología)
print ("El presupuesto para el área de Pediatría es de:", Presupuesto_Pediatría)
