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

def main():
    l=[5,6,2,8,9,1,3,4,7]
    print(l)
    print(insercion(l))
main()
