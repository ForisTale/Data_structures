from linked_list import LinkedList
from node import Node


class BidirectionalLinkedList(LinkedList):
    def __init__(self, head_node=None):
        super().__init__(head_node)
        if head_node is None:
            self.head_node = head_node
        else:
            self.head_node = BidirectionalNode(head_node)

    def add(self, value):
        node_to_add = BidirectionalNode(value)
        node_to_add.set_next_node(self.get_head_node())
        self.get_head_node().set_prev_node(node_to_add)
        self.head_node = node_to_add

    def remove_node(self, value):
        try:
            if self.get_head_node().get_value() == value:
                self.head_node = self.get_head_node().get_next_node()
                return
        except AttributeError:
            print("Error, can't find value in linked list to delete!")
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

    def pop(self, value_to_pop):
        node_to_pop = self.find(value_to_pop)
        if node_to_pop is None:
            return None
        elif node_to_pop is self.head_node:
            next_node = node_to_pop.get_next_node()
            if next_node is None:
                self.head_node = None
                return node_to_pop
            else:
                self.head_node = next_node
                next_node.set_prev_node(None)
                return node_to_pop

        prev_node = node_to_pop.get_prev_node()
        next_node = node_to_pop.get_next_node()
        if prev_node:
            prev_node.set_next_node(next_node)
        if next_node:
            next_node.set_prev_node(prev_node)

        return node_to_pop


class BidirectionalNode(Node):
    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value, next_node)
        self.next_node = next_node
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
