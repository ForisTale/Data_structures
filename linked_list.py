from node import Node


class LinkedList:
    def __init__(self, head_node=None):
        if head_node is None:
            self.head_node = head_node
        else:
            self.head_node = Node(head_node)

    def __iter__(self):
        current_node = self.get_head_node()

        while current_node:
            yield current_node.get_value()
            current_node = current_node.get_next_node()

    def get_head_node(self):
        return self.head_node

    def find(self, value_to_find):
        current_node = self.head_node

        while current_node:
            if current_node.get_value() == value_to_find:
                return current_node
            current_node = current_node.get_next_node()
        return None

    def traverse(self):
        current_node = self.get_head_node()
        value_list = []

        while current_node:
            value_list.append(current_node.get_value())
            current_node = current_node.get_next_node()

        return value_list
