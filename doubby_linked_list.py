"""    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA    
    - A lista encadeada é uma estrutura de dados formada por unidades      
        de informação chamadas nodos ou nós.    
    - Cada nodo da lista encadeada tem três partes: uma, que armazena a      
        informação; a segunda, que guarda o endereço do nodo anterior; e a      
        terceira, que guarda o endereço para o nodo seguinte da sequência    
    - A qualquer momento, temos um conhecimento apenas limitado de onde      
        se encontram todos os nodos da lista. Sabemos apenas onde está o      
        primeiro e o último nodo da sequência. Os nodos intermediários precisam      
        ser encontrados partindo-se do primeiro OU do último nodo e percorrendo      
        a sequência
"""

class Node:
    def __int__(self):
        self.prev = None # Ponteiro para o nodo anterior (None = nenhum)
        self.data = val  # Armazena a informação do usuário
        self.next = None # Ponteiro para o proximo nodo (None = nenhum)



class DoublyLinkedList: 
    def __init__(self):
        self.__head = None # (cabeça) Aponta para o incio da lista
        self.__tail = None # (cauda) Aponta para o fim da lista
        self.__count = 0   # Contador de nodos

    def is_empty(self):
        return self.__count == 0

    def insert(self, val):
        inserted = Node(val)

        # 1 caso: lista vazia
        if(self.is_empty()):
            self.__head = inserted
            self.__tail = inserted

        elif pos == 0:
            inserted.next = self.__head 
            self.__head.prev = inserted
            self.__head = inserted

        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # def to_str



lista = DoublyLinkedList()
print(lista.to_str())

lista.insert(0, 'Fusca')
print(lista.to_str)


lista.insert(0, 'Chevette')
print(lista.to_str)

lista.insert(3, 'Maverick')
print(lista.to_str)

       #self.__count += 1

