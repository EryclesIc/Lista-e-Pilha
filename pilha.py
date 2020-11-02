from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        # Adicionar um elemento da pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # Remover um elemento da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # Visualizar um elemento da pilha
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")
    def __repr__(self):
        return "[" + str(self.top)

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.pop()
# print(stack.peek())
# print(stack._size)
