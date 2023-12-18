class Node(object):
    def __init__(self) -> None:
        pass
    

class LinkedList(object):
    def __init__(self) :
        self.head = None
        self.tail = None
    def append(self, value):
        pass
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        pass
    def insert_at(idx, value):
        current = self.tail
        for _ in range(idx):
            current = current.next
            