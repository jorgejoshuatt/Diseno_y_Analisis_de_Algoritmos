class Queue:
    def __init__(self):
        self.__data=[]
        self.__size=0

    def get_length(self):
        return self.__size

    def is_empty(self):
        return self.__size==0

    def enqueue(self, value):
        self.__data.append(value)
        self.__size+=1

    def dequeue(self):
        return self.__data.pop(0) #validación que la lista no vacía

    def to_string(self):
        print (self.__data)

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



