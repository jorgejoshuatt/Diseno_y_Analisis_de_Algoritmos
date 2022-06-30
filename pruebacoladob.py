from adtcolas import DoubleQueue 
def main():
        cola=DoubleQueue()
        cola.add_first(5)
        cola.add_first(6)
        cola.add_first(7)
        print(f"{cola.to_string()}")
        cola.add_last(4)
        print(f"{cola.to_string()}")
        cola.delete_first()
        print(f"{cola.to_string()}")
        cola.delete_last()
        print(f"{cola.to_string()}")
        cola.add_first(7)
        print(f"{cola.to_string()}")
main()
    
