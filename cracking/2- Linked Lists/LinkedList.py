class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def insertBack(self, data):
        newNode = Node(data)
        pointer = self.head

        self.length += 1
        if not pointer:
            self.head = newNode
            return
        while pointer.next:
            pointer = pointer.next
        pointer.next = newNode
        return newNode

    def insertFront(self, data):
        self.length += 1
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def print(self):
        if not self.head: return
        aux = self.head
        while aux != None:
            if aux.next == None: print(aux.data)
            else: print(str(aux.data) + '->', end = '')
            aux = aux.next

    def reverse(self):
        p1 = self.head
        l2 = LinkedList()
        while p1:
            l2.insertFront(p1.data)
            p1 = p1.next
        return l2