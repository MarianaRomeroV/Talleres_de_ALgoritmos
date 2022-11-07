lista=[1,2,3,4,5,1]
lista2=["🤣","💕","😒","😍"]
lista3=[1,3,4,6,8,9,0,6,5,]
#Agregar al final
lista.append(50)
#Eliminar al final o en una posición
lista.pop()
lista.pop()
#Agregar un elemento en una posición
lista.insert(0,"😊")
lista.insert(4,"😊")
#contar cuantos elementos hay
a=lista.count("😊")
#sacar la posición de un elemento 
p=lista.index("😊")
#copiar la lista
copia=lista.copy()
#Unir las listas
lista.extend(lista2)
#Ordenar una lista de manera asc
lista3.sort(reverse=True)
lista3.clear()
lista2.remove("🤣")
lista2.reverse()
print(lista2)