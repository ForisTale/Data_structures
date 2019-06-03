from linked_list import LinkedList
from node import Node


class UnidirectionalLinkedList(LinkedList):

    def add(self, value):
        node_to_add = Node(value)
        node_to_add.set_next_node(self.head_node)
        self.head_node = node_to_add

    def remove_node(self, value_to_remove):
        try:
            if value_to_remove == self.get_head_node().get_value():
                self.head_node = self.get_head_node().get_next_node()
                return
        except AttributeError:
            print("Error, can't find value in linked list to delete!")
            return

        current_node = self.get_head_node()
        while current_node:
            try:
                if current_node.get_next_node().get_value() == value_to_remove:
                    node_to_set = current_node.get_next_node().get_next_node()
                    current_node.set_next_node(node_to_set)
                    return
            except AttributeError:
                print("Error, can't find value in linked list to delete!")
            current_node = current_node.get_next_node()

    def pop(self, value_to_pop):
        current_node = self.get_head_node()
        if current_node is None:
            return
        elif current_node.get_value() == value_to_pop:
            self.head_node = current_node.get_next_node()
            return current_node

        while current_node:
            try:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_pop:
                    node_after_next_node = next_node.get_next_node()
                    current_node.set_next_node(node_after_next_node)

                    return next_node

            except AttributeError:
                return

            current_node = current_node.get_next_node()
