class TripleNodo:
    def __init__(self, value, up=None, centro=None, down=None):
        self.data=value
        self.up=up #nodo arriba
        self.centro=centro #nodo centro
        self.down=down #nodo abajo
        
def main():
    #nodo principal
    head=TripleNodo(20)
    #agregando nodos centrales
    head.centro=TripleNodo(19)
    head.centro.down=TripleNodo(67)
    head.centro.down=TripleNodo(99)
    #agregando nodos de arriba
    head.up=TripleNodo(23)
    head.up.centro=TripleNodo(57)
    #Sin nodos abajo
    #imprimir 99 y 57
    print(f"{head.centro.down.data}")
    print(f"{head.up.centro.data}")
main()
