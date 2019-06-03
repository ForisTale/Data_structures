from unidirectional_linked_list import UnidirectionalLinkedList as LinkedList


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for _ in range(array_size)]

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_point = self.array[array_index]

        if current_point.get_head_node() is None:
            current_point.add((key, value))
            return
        elif current_point.get_head_node().get_value()[0] == key:
            current_point.get_head_node().set_value((key, value))




    def retrieve(self, argument):
        pass

    @staticmethod
    def hash(key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size
