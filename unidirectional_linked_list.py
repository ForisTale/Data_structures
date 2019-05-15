

class UnidirectionalLinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def add_node(self, node):
        node.set_link_node(self.head_node)
        self.head_node = node

    def get_head_node(self):
        return self.head_node

    def __iter__(self):
        current_node = self.get_head_node()

        while current_node:
            yield current_node.get_value()
            current_node = current_node.get_link_node()

    def remove_node(self, value_to_remove):
        if value_to_remove == self.get_head_node().get_value():
            self.head_node = self.get_head_node().get_link_node()
            return

        current_node = self.get_head_node()
        while current_node:
            try:
                if current_node.get_link_node().get_value() == value_to_remove:
                    node_to_set = current_node.get_link_node().get_link_node()
                    current_node.set_link_node(node_to_set)
                    return
            except AttributeError:
                print("Error, can't find value in linked list to delete!")
            current_node = current_node.get_link_node()



