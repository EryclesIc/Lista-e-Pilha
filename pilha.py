def pop(self):
    #Remover um elemento da pilha
    if self.size > 0:
        node = self.top
        self.top = self.top.next
        self._size = self.size - 1
        return node.data
    raise IndexError("The stack is empty")

def peek(self):
    #Visualizar um elemento da pilha
    if self._size > 0:
            return self.top.data
    raise IndexError("The stack is empty")

class Node:
    def _init_(self, data) :
        self.data = data
        self.next = None