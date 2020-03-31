# Implement an algorithm to find the kth to last element of a singly linked list

from LinkedList import LinkedList

class Solution:

    """
    O(n), O(n)
    """
    def returnKthToLast(self, l1: LinkedList, k: int):
        if l1.length < k:
            print('Erro')
            return
        
        p1 = l1.head
        index = 0
        while index < k:
            p1 = p1.next
            index += 1
        newLinkedList = LinkedList()
        newLinkedList.head = p1
        newLinkedList.length = l1.length - k
        newLinkedList.print()

l1 = LinkedList()
l1.insertBack('a')
l1.insertBack('b')
l1.insertBack('c')
l1.insertBack('a')
l1.insertBack('d')
l1.insertBack('b')
l1.insertBack('d')
l1.insertFront('k')

solve = Solution()
k = 3
solve.returnKthToLast(l1, k)