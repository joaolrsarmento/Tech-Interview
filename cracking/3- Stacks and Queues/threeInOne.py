# Describe how you could use a single array to implement three stacks


from stack import Stack, StackNode

class Solution:
    def threeInOne(self, s: Stack):
        # Pretty damn simple
        pass

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
solve.threeInOne(s)