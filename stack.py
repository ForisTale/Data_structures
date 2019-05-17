

class StackIsFull(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class Stack:

    def __init__(self, limit=0):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def push(self, node):
        if self.has_space():
            node.set_next_node(self.top_item)
            self.top_item = node
            self.size += 1
        else:
            raise StackIsFull

    def has_space(self):
        if self.limit:
            return self.size < self.limit
        else:
            return True

    def peek(self):
        if not self.is_empty():
            return self.top_item.value
        else:
            return "Stack is empty!"

    def pop(self):
        if not self.is_empty():
            value_to_return = self.top_item.value
            self.top_item = self.top_item.get_next_node()
            self.size -= 1
            return value_to_return
        else:
            raise StackIsEmpty

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
