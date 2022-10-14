#entradas
A = int(input("Ingrese el valor del coeficiente A: "))
B = int(input("Ingrese el valor del coeficiente B: "))
C = int(input("Ingrese el valor del coeficiente C: "))
D = (B**2)-(4*A*C)
#caja negra
if (D == 0):
    X1 =(-B)/(2*A)
    print(f"Como D = {D}, entonces x1= x2= {X1}")
elif(D > 0):
    X1 = ((-B) + (((B**2)-4*A*C) / (2*A)) ** (1/2))
    X2 = ((-B) - (((B**2) - (4 * A * C) / (2 * A)) ** (1/2)))
    print(f"D = {D}, entonces X1 = {X1} y X2 = {X2}")
elif D < 0:
    print(f"Como D = {D} < 0, entonces NO tiene solucion en los reales")