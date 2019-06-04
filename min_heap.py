

class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.size = 0

    def add(self, value):
        self.heap_list.append(value)
        self.size += 1
        self.heapify_up()

    def retrieve_min(self):
        if self.size < 1:
            return
        self.swap(1, self.size)
        min_value = self.heap_list.pop()
        self.size -= 1
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
        while self.has_child(index):
            index_of_smaller = self.get_smaller_child(index)
            if self.heap_list[index] > self.heap_list[index_of_smaller]:
                self.swap(index, index_of_smaller)
            index = index_of_smaller

    def get_smaller_child(self, index):
        right_index = self.right_index(index)
        left_index = self.left_index(index)

        if right_index > self.size:
            return left_index

        if self.heap_list[left_index] < self.heap_list[right_index]:
            return left_index
        else:
            return right_index

    @staticmethod
    def parent_index(index):
        return index // 2

    @staticmethod
    def left_index(index):
        return index * 2

    @staticmethod
    def right_index(index):
        return index * 2 + 1

    def has_child(self, index):
        return self.left_index(index) <= self.size

    def swap(self, first, second):
        self.heap_list[first], self.heap_list[second] = self.heap_list[second], self.heap_list[first]
