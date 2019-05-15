from linked_list import LinkedList
from node import Node


class BidirectionalLinkedList(LinkedList):

    def add_node(self, node_to_add):
        node_to_add.set_link_node(self.get_head_node())
        self.get_head_node().set_prev_node(node_to_add)
        self.head_node = node_to_add


class BidirectionalNode(Node):
    def __init__(self, value, next_node=None, prev_node=None):
        self.link_node = next_node
        self.value = value
        self.prev_node = prev_node

    def get_next_node(self):
        return self.link_node

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.link_node = next_node
