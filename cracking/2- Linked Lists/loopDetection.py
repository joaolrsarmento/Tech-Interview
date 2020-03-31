# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop

from LinkedList import LinkedList

class Solution:
    def loopDetection(self, l1: LinkedList):
        mySet = set()

        p1 = l1.head
        while p1:
            if p1 not in mySet:
                mySet.add(p1)
            else:
                return p1.data
            p1 = p1.next

        return False

l1 = LinkedList()
l1.insertBack(2)
l1.insertBack(3)
l1.insertBack(5)
l1.insertBack(4)

l1.head.next.next.next.next = l1.head # Creates loop

solve = Solution()
print(solve.loopDetection(l1))