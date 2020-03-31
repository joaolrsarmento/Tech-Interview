# How would you design a stack which, in addition to push and pop, has a function min.
# Push, Pop and Min should be O(1) time.

from stack import Stack, StackNode

class StackMin(object):

    """
    We can use an extra stack that stores the minimums.
    Let's call the main stack S1 and the extra stack S2.
    If we push a node through S1 and that node is not the minimum, we don't store it 
    in S2. Basically, that means that the minimum is the new node.
    And, if we pop an element from S1 and that element is not equal to the top of S2,
    that means that the actual minimum is below the popped element, so, we should not change S2.
    """

    def __init__(self):
        self.top = StackNode()
        self.stackMin = Stack()

    def push(self, node):
        if not self.top or node.data < self.top.data:
            self.stackMin.push(node)

        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        if node.data == self.stackMin.peek():
            self.stackMin.pop()
        self.top = self.top.next
        return node.data

    def peek(self):
        return self.top.data

    def min(self):
        return self.stackMin.peek()