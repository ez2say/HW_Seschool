class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DeQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, data):
        assert data is not None, ValueError
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def insert_rear(self, data):
        assert data is not None, ValueError
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def delete_front(self):
        assert self.front is not None, Exception("Ошибочка")
        data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return data

    def delete_rear(self):
        assert self.rear is not None, Exception("Ошибочка")
        data = self.rear.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return data

    def is_empty(self):
        return self.front is None

    def peek_front(self):
        assert self.front is not None, Exception("Ошибочка")
        return self.front.data

    def peek_rear(self):
        assert self.rear is not None, Exception("Ошибочка")
        return self.rear.data