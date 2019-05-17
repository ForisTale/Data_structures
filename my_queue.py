from node import Node


class QueueIsEmpty(Exception):
    pass


class QueueIsFull(Exception):
    pass


class Queue:

    def __init__(self, limit=0):
        self.head = None
        self.tail = None
        self.limit = limit
        self.size = 0

    def enqueue(self, value_to_enqueue):
        if self.has_space():
            if self.head is None:
                new_node = Node(value_to_enqueue)
                self.head = new_node
                self.tail = new_node
                self.size += 1
            else:
                new_node = Node(value_to_enqueue)
                new_node.set_next_node(self.head)
                self.head = new_node
                self.size += 1
        else:
            raise QueueIsFull

    def has_space(self):
        if self.limit:
            return self.size < self.limit
        else:
            return True

    def dequeue(self):
        if not self.is_empty():
            value_to_return = self.tail.value
            if self.head is self.tail:
                self.head = None
                self.tail = None
                self.size -= 1
                return value_to_return
            else:
                current_node = self.head
                while True:
                    if current_node.get_next_node() is self.tail:
                        self.tail = current_node
                        self.size -= 1
                        return value_to_return
                    current_node = current_node.get_next_node()
        else:
            raise QueueIsEmpty

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def peek(self):
        return self.head.value
