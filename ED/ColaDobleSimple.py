class DoubleQueue:
    def __init__(self):
        self.__data=[]
        self.__size=0

    def add_first(self,value):
        self.__data.append(value)
        self.__size+=1
    def add_last(self,value):
        self.__data.insert(0,value)
        self.__size+=1
    def delete_first(self):
        return self.__data.pop()
    
    def delete_last(self):
        return self.__data.pop(0)

    def is_empty(self):
        return self.__size==0

    def get_length(self):
        return self.__size

    def to_string(self):
        return self.__data

def main():
        cola=DoubleQueue()
        cola.add_first(1)
        cola.add_first(2)
        cola.add_first(7)
        cola.add_first(8)
        print(f"{cola.to_string()}")
        cola.add_last(4)
        cola.add_last(18)
        print(f"{cola.to_string()}")
        cola.delete_first()
        print(f"{cola.to_string()}")
        cola.delete_last()
        print(f"{cola.to_string()}")
        cola.add_first(5)
        print(f"{cola.to_string()}")
main()
