class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_at_head(self, data):
        assert isinstance(data, int), TypeError
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_tail(self, data):
        assert isinstance(data, int), TypeError
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def remove_from_tail(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def search(self, data):
        assert isinstance(data, int), TypeError
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False