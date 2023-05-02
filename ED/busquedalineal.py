def busquedalineal(lista, dato):
    pos = 0
    encontrado = False
    while pos < len(lista) and not encontrado:
        if lista[pos] == dato:
            encontrado = True
        else:
            pos = pos+1	
    if encontrado==True:
        return(f"El número ha sido encontrado y está en la posición {pos}")
    else:
        return("El número no ha sido encontrado")



lista=[]
n=int(input("Número de elementos en la lista: "))
for i in range (0,n):
    a=int(input("Agregue un número: "))
    lista.append(a)
b=int(input("¿Qué número desea buscar? "))
print(busquedalineal(lista, b))

