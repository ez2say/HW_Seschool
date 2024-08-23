class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        assert isinstance(data, int), TypeError
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        assert isinstance(data, int), TypeError
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        assert isinstance(key, int), TypeError
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        assert isinstance(key, int), TypeError
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count




