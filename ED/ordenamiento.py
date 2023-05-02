def burbuja(lista):
    for tope in range(len(lista)-1, 0, -1):
        for cursor in range(tope):
            if lista[cursor]>lista[cursor+1]:
                aux=lista[cursor]
                lista[cursor]=lista[cursor+1]
                lista[cursor+1]=aux
    return lista


def seleccion(lista):
    for pivote in range(0,len(lista)-2,1):
        menor=pivote
        for index in range(pivote,len(lista),1):
            if lista[index] < lista[menor]:
                menor=index
        lista[pivote],lista[menor]=lista[menor],lista[pivote]
    return lista

def insercion(lista):
    for pivote in range(1,len(lista),1):
        for index in range(pivote):
            if lista[pivote] < lista[index]:
                tmp=lista[index]
                lista[index]=lista[pivote]
                #recorrer a la derecha
                for i in range(index+1,pivote+1,1):
                    tmp2=lista[i]
                    lista[i]=tmp
                    tmp=tmp2
    return lista

def busqueda_lineal(data,valor):
    for index in range(len(data)):
        if data[index]==valor:
            return index
    return None

def busqueda_binaria(data,value):
    ini=0
    fin=len(data)-1
    for i in range(len(data)):
        medio=(ini+fin)/2
        if value==data[medio]:
            return i
        elif value<data[medio]:
            fin=medio
        else:
            ini=medio
        
def main():
    l=[3,8,9,5,0]
    print(burbuja(l))
    print(seleccion(l))
    nombres=['carlos','enrique','zoila','alberto','benita','diana']
    print(seleccion(nombres))
    print(insercion(l))
    print(busqueda_lineal(l,0))
main()

#ordenamiento por inserción y selección
