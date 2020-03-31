# Given two linked lists, return a linked list which sum the sum of the linked lists inputed.

from LinkedList import LinkedList

class Solution:
    def sumLists(self, l1: LinkedList, l2: LinkedList) -> (LinkedList, int):
        """
        Solves in O(n), O(n)
        
        """
        p1, p2 = l1.head, l2.head
        l3 = LinkedList()
        carry, out = 0,0
        while p1 or p2:
            x = p1.data if p1 else 0
            y = p2.data if p2 else 0
            carry, out = divmod(x + y + carry, 10)
            l3.insertBack(out)
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        if carry:
            l3.insertBack(carry)
        
        
        exp = 0
        s = 0
        p3 = l3.head
        while p3:
            s += p3.data * 10 ** exp
            exp += 1
            p3 = p3.next
        
        l3.print()
        print(s)
        return l3, s

l1 = LinkedList()
l2 = LinkedList()
l1.insertBack(7)
l1.insertBack(1)
l1.insertBack(6)
l2.insertBack(5)
l2.insertBack(9)
l2.insertBack(2)
l2.insertBack(2)

solve = Solution()

solve.sumLists(l1,l2)