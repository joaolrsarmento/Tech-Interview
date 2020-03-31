# Implement a set of stacks that has a maximum capacity for each stack.
# Also, implement a popAt(int index) function that manages to access the index-th stack.

from stack import Stack, StackNode


class SetOfStacksNode:
    def __init__(self):
        self.stack = Stack()
        self.nextStack = None

class SetOfStacks:
    def __init__(self, maximumCapacity):
        self.maximumCapacity = maximumCapacity
        self.headStack = SetOfStacksNode()

    def push(self, data):
        if self.headStack.stack.length < self.maximumCapacity:
            self.headStack.stack.push(StackNode(data))
        else:
            setOfStacksNode = SetOfStacksNode()
            setOfStacksNode.nextStack = self.headStack.stack
            self.headStack = setOfStacksNode
            self.headStack.stack.push(StackNode(data))
    def pop(self):
        return self.headStack.stack.pop()
    def peek(self):
        return self.headStack.stack.peek()
    def popAt(self, index):
        cont = 0
        p1 = self.headStack.stack

        while p1 and cont < index:
            p1 = p1.nextStack

        return p1.stack.pop()