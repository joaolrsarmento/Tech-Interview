# Implements a LIFO Queue

class StackNode:
    def __init__(self):
        pass
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__top = None
        self.length = 0

    def push(self, node: StackNode):
        self.length += 1
        node.next = self.__top
        self.__top = node

    def peek(self):
        return self.__top.data
    
    def pop(self):
        self.length -= 1
        top = self.__top
        self.__top = self.__top.next
        return top.data

    def isEmpty(self):
        return False if self.__top else True