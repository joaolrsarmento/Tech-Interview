# Implements a FIFO Queue

class QueueNode:
    def __init__(self):
        pass
    def __init__(self, data):
        self.data = data
        self.next = QueueNode()

class Queue:
    def __init__(self):
        self.first = QueueNode()
        self.last = self.first

    def add(self, node):
        if not self.first:
            self.first, self.last = node, node
            return
        self.last.next = node
        self.last = self.last.next
        
    def remove(self):
        self.first = self.first.next
    
    def peek(self):
        return self.first.data

    def isEmpty(self):
        return True if self.first else False
    
