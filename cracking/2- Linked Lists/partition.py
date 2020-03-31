# Write code to partition a linked list around a value x, such
# that all nodes less than x come before all nodes greater than or equal to x.
# If x is in the list, the values of x only need to be after the elements less than x.
# The partition element x can appear anywhere in the right partition, it doesn't need to appear
# between the left and right partitions.

# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, x = 5
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from LinkedList import LinkedList

class Solution:
    """
    Solves in O(n), O(n) 
    """
    def insertAfter(self, p1, p2):
        p2.next = p1.next
        p1.next = p2
    def partition(self, l1: LinkedList, x):
 
        before = LinkedList()
        after = LinkedList()
        p1 = l1.head
        while p1:
            if p1.data < x:
                beforeLastNode = before.insertBack(p1.data)
                
            else:
                afterLastNode = after.insertBack(p1.data)
            p1 = p1.next

        beforeLastNode.next = after.head
        before.print()
        return before.head
l1 = LinkedList()
l1.insertBack(3)
l1.insertBack(5)
l1.insertBack(8)
l1.insertBack(5)
l1.insertBack(10)
l1.insertBack(2)
l1.insertBack(1)
x = 5

solve = Solution()
solve.partition(l1, x)