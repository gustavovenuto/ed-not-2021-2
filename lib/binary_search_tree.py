

class Node:
    def __init__(self, val):
        self.data = vala
        self.left = None
        self.right = None



class BinarySearchTree:

    """
        Construtor da classe
    """
    
    def __init__(self):
        self.__root = None # Raiz da arvore

    def insert(self, val):

        inserted = Node(val)

        if self.__root is None: self.__root = inserted

    def __insert__node(node, root):
        if node.data < root.data: 
            if root.left is None: root.left = node
        else:
            if root.right is None: root.right = none