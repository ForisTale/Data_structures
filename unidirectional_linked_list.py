

class UnidirectionalLinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def add_node(self, node):
        node.set_link_node(self.head_node)
        self.head_node = node

    def get_head_node(self):
        return self.head_node
