from adtcolas import Queue
def main():

    cola=Queue()
    cola.enqueue(2)
    cola.enqueue(6)
    cola.enqueue(36)
    cola.enqueue(34)
    cola.enqueue(64)
    cola.enqueue(2)
    print(f"Sacar={cola.dequeue()}")
    print(f"Sacar={cola.dequeue()}")
    cola.enqueue(20)
    cola.enqueue(30)
    print(f"Sacar={cola.dequeue()}")
main()
