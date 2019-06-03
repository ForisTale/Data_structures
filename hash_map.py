from unidirectional_linked_list import UnidirectionalLinkedList as LinkedList


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for _ in range(array_size)]

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        array_item = self.array[array_index]
        current_node = array_item.get_head_node()

        if current_node is None:
            array_item.add((key, value))
            return

        while current_node:
            if current_node.get_value()[0] == key:
                current_node.set_value((key, value))
            elif current_node.get_next_node() is None:
                array_item.add((key, value))
                return

            current_node = current_node.get_next_node()

    def retrieve(self, argument):
        pass

    @staticmethod
    def hash(key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size
