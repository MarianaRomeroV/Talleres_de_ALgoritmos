#entradas
a= []
total = 0
#caja negra
for i in range(1, 13):
    n= (5 * i) + 1
    a.append(n)
for i in range(12):
    total += a[i]
print(f"El doceavo elemento de la sucesión es: {a[11]}")
print(f"La sumatoria es: {total}")