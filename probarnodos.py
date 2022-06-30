from listas_enlazadas import Nodo
def main():
    """
    head=Nodo()
    head.data=10
    head.next.data=20
    print(head.data)
    print(head.next.data)
    """
    """
    head=Nodo(10)
    head.next=Nodo(20)
    head.next.next=Nodo(30)
    head.next.next.next=Nodo(40)
    head.next.next.next.next=Nodo(50)
    """
    head=Nodo(10,Nodo(20,Nodo(30,Nodo(40,Nodo(50)))))
    print(head.next.next.next.data)
    nodo_actual=head
    while nodo_actual.next != None:
        print(f"{nodo_actual.data} --> ", end="")
        nodo_actual=nodo_actual.next
    print(nodo_actual.data)
main()
