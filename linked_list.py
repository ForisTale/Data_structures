

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def __iter__(self):
        current_node = self.get_head_node()

        while current_node:
            yield current_node.get_value()
            current_node = current_node.get_link_node()

    def get_head_node(self):
        return self.head_node
