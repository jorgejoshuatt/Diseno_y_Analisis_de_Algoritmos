class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value
        self.next=siguiente
class ListaEnlazada:
    def __init__(self):
        self.__head=None
        
    def is_empty(self):
        return self.__head==None

    def get_tail(self):
        nodo_actual=self.__head
        #verificar que la lista no esté vacía 
        while nodo_actual.next != None:
            nodo_actual=nodo_actual.next
        return nodo_actual

    def append(self,value):
        if self.is_empty():
            self.__head=Nodo(value)
        else:
            self.get_tail().next=Nodo(value)
            
    def transversal(self):
        nodo_actual=self.__head
        while nodo_actual.next !=None:
            print(f"{nodo_actual.data} --->", end="")
            nodo_actual=nodo_actual.next
        print(nodo_actual.data)
        
    def remove(self,value):
        nodo_actual=self.__head
        previo=nodo_actual
        while nodo_actual.data!=value or nodo_actual.next==None:
            previo=nodo_actual
            nodo_actual=nodo_actual.next
        if nodo_actual.data==value:
            previo.next=nodo_actual.next
            nodo_actual=None
            return True
        elif nodo_actual.data==None:
            return False
    
    def pop(self):
        pass        

