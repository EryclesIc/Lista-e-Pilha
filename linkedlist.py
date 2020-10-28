from node import Node
# sequencial = []
# sequencial.append(7)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def get(self, index):
        # a = lista.get(6)
        pass

    def set(self, indez, elem):
        # lista.set(5, 9)
        pass

    def __getitem__(self, index):
        # a = lista[5]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[5] = 9
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Retorna o indice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))