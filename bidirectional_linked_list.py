from linked_list import LinkedList
from node import Node


class BidirectionalLinkedList(LinkedList):

    def add_node(self, node_to_add):
        node_to_add.set_link_node(self.get_head_node())
        self.get_head_node().set_prev_node(node_to_add)
        self.head_node = node_to_add

    def remove_node(self, value):
        if self.get_head_node().get_value() == value:
            self.head_node = self.get_head_node().get_next_node()
            return
        current_node = self.get_head_node()
        while current_node:
            try:
                if current_node.get_next_node().get_value() == value:
                    next_node = current_node.get_next_node().get_next_node()
                    next_node.set_prev_node(current_node)
                    current_node.set_next_node(next_node)
                    return
            except AttributeError:
                print("Error, can't find value in linked list to delete!")
            current_node = current_node.get_next_node()


class BidirectionalNode(Node):
    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value)
        self.link_node = next_node
        self.prev_node = prev_node

    def get_next_node(self):
        return self.link_node

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.link_node = next_node
