# Write code to remove duplicates from an unsorted linked list
# How would you solve if a temporary buffer is not allowed?

from LinkedList import LinkedList

class Solution:

    """
    Solves in O(n)
    If no buffer is allowed, we can do it in O(n^2) comparing just each element
    """
    
    def removeDupsWithBuffer(self, l1: LinkedList):
        """
        O(n), O(n)
        """
        if not l1.head:
            print("Empty")
            return

        hashTable = {}
        aux = l1.head
        index = 0
        hashTable[aux.data] = index

        while aux.next != None:

            index += 1
            if hashTable.get(aux.next.data, -1) != -1:
                aux.next = aux.next.next
            else:
                hashTable[aux.next.data] = index
                aux = aux.next
        l1.print()

        return

    def removeDupsWithoutBuffer(self, l1: LinkedList):
        """
        O(n^2), O(1)
        """
        if not l1.head:
            print("Empty")
            return
        p1 = l1.head
        while p1:
            p2 = p1
            while p2.next:
                if p1.data == p2.next.data:
                    p2.next = p2.next.next
                else:
                    p2 = p2.next
            p1 = p1.next
        l1.print()
        return

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

solve.removeDupsWithoutBuffer(l1)