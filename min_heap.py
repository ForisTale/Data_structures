

class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.size = 0

    def add(self, value):
        self.heap_list.append(value)
        self.size += 1
        self.heapify_up()

    def retrieve_min(self):
        self.heap_list[1], self.heap_list[self.size] = self.heap_list[self.size], self.heap_list[1]
        min_value = self.heap_list.pop()
        self.heapify_down()

        return min_value

    def heapify_up(self):
        index = self.size

        while self.parent_index(index) > 0:
            child = self.heap_list[index]
            parent = self.heap_list[self.parent_index(index)]
            if parent > child:
                self.heap_list[index] = parent
                self.heap_list[self.parent_index(index)] = child
            index = self.parent_index(index)

    def heapify_down(self):
        index = 1


    @staticmethod
    def parent_index(index):
        return index // 2

    @staticmethod
    def left_index(index):
        return index * 2

    @staticmethod
    def right_index(index):
        return index * 2 + 1
