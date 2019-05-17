

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "Node with value: " + str(self.value)

    def get_value(self):
        return self.value

    def set_next_node(self, link_node):
        self.next_node = link_node

    def get_next_node(self):
        return self.next_node
