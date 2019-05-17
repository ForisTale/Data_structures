from linked_list import LinkedList


class UnidirectionalLinkedList(LinkedList):

    def add_node(self, node):
        node.set_next_node(self.head_node)
        self.head_node = node

    def remove_node(self, value_to_remove):
        if value_to_remove == self.get_head_node().get_value():
            self.head_node = self.get_head_node().get_next_node()
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



