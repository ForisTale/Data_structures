

class MinHeap:
    def __init__(self):
        self.heap = [None]

    def add(self, value):
        self.heap.append(value)
        self.heapify_up()

    def retrieve(self):
        pass

    def heapify_up(self):
        pass

    @staticmethod
    def parent_index(index):
        return index // 2

    @staticmethod
    def left_index(index):
        return index * 2

    @staticmethod
    def right_index(index):
        return index * 2 + 1
