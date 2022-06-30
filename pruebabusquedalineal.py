def busqueda_lineal(dato,valor):
    for index in range(len(dato)):
        if dato[index]==valor:
            return index
    return None
def main():
    l=[0,1,2,3,4,5]
    print(l)
    print(busqueda_lineal(l,3))
main()
