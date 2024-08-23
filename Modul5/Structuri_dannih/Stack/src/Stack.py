class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        assert data is not None, ValueError
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        assert not self.is_empty(), "ПустоТут"
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        assert not self.is_empty(), "ПустоТут"
        return self.top.data