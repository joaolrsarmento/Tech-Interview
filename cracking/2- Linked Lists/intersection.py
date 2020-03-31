# Given two singly linked lists, determine if the two lists intersect and return the intersection node.
# Consider intersection per reference

from LinkedList import LinkedList
import queue

class Solution:
    def intersection(self, l1: LinkedList, l2: LinkedList) -> Node:
        """ 
        Solves in O(A + B), O(1)
        """
        result1 = self.getTailAndSize(l1)
        result2 = self.getTailAndSize(l2)
        if result1[0] != result2[0]: return False

        shorter = l1.head if l1.length <= l2.length else l2.head
        longer = l2.head if l1.length <= l2.length else l1.head

        longer = self.getKthNode(longer, abs(l1.length - l2.length))

        while shorter != longer:
            shorter = shorter.next
            longer = longer.next

        return shorter
    def getTailAndSize(self, l1: LinkedList) -> (Node, int):
        p1 = l1.head
        while p1.next:
            p1 = p1.next
        return p1, l1.length
    def getKthNode(self, l1: LinkedList, k: int) -> Node:
        cont = 0
        p1 = l1.head
        while cont < k:
            p1 = p1.next
        return p1
        
l1, l2 = LinkedList(), LinkedList()
l1.insertBack(3)
l1.insertBack(5)
l1.insertBack(8)
l2.insertBack(5)
l2.insertBack(8)
l2.insertBack(5)
l2.insertBack(3)


solve = Solution()
print(solve.intersection(l1, l2))