class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("пустоТут")
        data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("пустоТут")
        return self.front.data