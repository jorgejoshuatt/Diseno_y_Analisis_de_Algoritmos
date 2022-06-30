def seleccion(lista):
    for pivote in range(0,len(lista)-1,1):
        menor=pivote
        for index in range(pivote,len(lista),1):
            if lista[index] < lista[menor]:
                menor=index
        lista[pivote],lista[menor]=lista[menor],lista[pivote]
    return lista
def busqueda_binaria(lista, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = lista[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_binaria(lista, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_binaria(lista, busqueda, indiceDelElementoDelMedio + 1, derecha)
 


def main():
    lista=[23,765,32,778,477,34,6,78,79,12,3,314,1456,2,90,8]
    print(lista)
    print(seleccion(lista))
    n=int(input("Ingrese el número que quiere buscar dentro de la lista: "))
    x=busqueda_binaria(lista,n,0,len(lista)-1)
    if x==-1:
        print("El número no existe en la lista")
    else:
        print(f"El número buscado se encuentra en la lista y está en la posición {x}")
main()
