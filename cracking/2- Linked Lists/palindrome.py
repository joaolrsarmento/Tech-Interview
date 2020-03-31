# Implement a funciton to check if a linked list is a palindrome

from LinkedList import LinkedList
import queue

class Solution:
    def palindromeReversing(self, l1: LinkedList):
        """
        Solves in O(n), O(n)
        """
        l2 = l1.reverse()
        p1 = l1.head
        p2 = l2.head

        while p1 and p2:
            if p1.data != p2.data:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def palindromeCheckingHalf(self, l1: LinkedList):
        """
        Solves in O(n), O(n)
        """
        slow = l1.head
        fast = l1.head
        stack = queue.LifoQueue()

        while fast and fast.next:
            stack.put(slow.data)
            slow = slow.next
            fast = fast.next.next

        if fast:
            print(slow.data)
            slow = slow.next

        while not stack.empty() and slow:
            top = stack.get()
            if top != slow.data:
                return False
            slow = slow.next
        return True
        
l1 = LinkedList()
l1.insertBack(3)
l1.insertBack(5)
l1.insertBack(8)
l1.insertBack(5)
l1.insertBack(8)
l1.insertBack(5)
l1.insertBack(3)


solve = Solution()
print(solve.palindromeCheckingHalf(l1))