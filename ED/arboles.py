class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.data=value
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.__root=None

    def insert(self,value):
        if self.__root==None:
            self.__root=TreeNode(value)
        else:
            """
            if value<self.__root.data:
                self.__root.left=TreeNode(value)
            elif value>self.__root.data:
                self.__root.right=TreeNode(value)
            else:
                pass
                """
            self.__insert_recursivo(self.__root,value)

            
    def __insert_recursivo(self,nodo,value):
        if nodo.data==value:
            pass
        elif value<nodo.data:
            if nodo.left==None:
                nodo.left=TreeNode(value)
            else:
                self.__insert_recursivo(nodo.left,value)
        else:
            if nodo.right==None:
                nodo.right=TreeNode(value)
            else:
                self.__insert_recursivo(nodo.right,value)

        
    def remove(self,value):
        pass
    def search(self,value):
        pass
    def transversal(self,formato):
        if formato=='in':
            self.__recorrido_in(self.__root)
        elif formato=='pre':
            self.__recorrido_pre(self.__root)
        else:
            self.__recorrido_pos(self.__root)

    def __recorrido_in(self,nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data)
            self.__recorrido_in(nodo.right)

    def __recorrido_pre(self,nodo):
        if nodo != None:
            print(nodo.data)
            self.__recorrido_in(nodo.left)
            self.__recorrido_in(nodo.right)

    def __recorrido_pos(self,nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            self.__recorrido_in(nodo.right)
            print(nodo.data)
        
