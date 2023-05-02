class nodo:
    def __init__(self,value,siguiente=None):
        self.data=None
        self.next=None

#proximamente
class ListaEnlazada:
    def __init__(self):
        self.__head=None
    def is_empty():
        return self.__head==None
        
    def get_tail():
        nodo_actual=self.__head
        #Verificar que la lista no este vacia
        while nodo_actual.next!=None:
            nodo_actual=nodo_actual.next
        return nodo_actual
    
    def append():
        if self.is_empty():
            self.__head==Nodo(value)
        else:
            self.get_tail().next=Nodo(value)
        
    def prepend(self,value):
        if self.is_empty():
            self.__head==Nodo(value)
        else:
            self.__head=Nodo(value,self.__head) 
            
    def add_after(self):
        pass
    def add_before(self):
        pass
    def transversal(self):
        nodo_actual=self.__head
        while nodo_actual.next!=None:
            print(f"{nodo_actual.data}-->")
            nodo_actual=nodo_actual.next
            print(nodo_actual.data)
        
    def remove(self):
        pass
    def pop(self):
        pass
