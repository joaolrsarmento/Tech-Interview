# Write a program to sort a stack such that the smallest items are on top. You only can use an additional
# temporary stack, but you can copy elements into other data structure.
# Only operations available on the stack: push, pop, peek, isEmpty

from stack import Stack, StackNode

class Solution:
    def sortStack(self, s1: Stack):
        """
        Solves in O(n^2), O(n).
        For each element in s1, we find its correct position.
        """
        s2 = Stack()
        while not s1.isEmpty():
            tmp = s1.pop()
            while not s2.isEmpty() and s2.peek() > tmp:
                s1.push(StackNode(s2.pop()))
            s2.push(StackNode(tmp))
        
        while not s2.isEmpty():
            s1.push(StackNode(s2.pop()))

        while not s1.isEmpty():
            print(s1.pop())

s = Stack()
node = StackNode(1)
s.push(node)
node = StackNode(2)
s.push(node)
node = StackNode(3)
s.push(node)
node = StackNode(4)
s.push(node)
node = StackNode(5)
s.push(node)
node = StackNode(6)
s.push(node)

solve = Solution()
solve.sortStack(s)