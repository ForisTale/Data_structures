

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
        index_of_smaller = self.get_smaller_child(index)


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

    def swap(self, first, second):
        self.heap_list[first], self.heap_list[second] = self.heap_list[second], self.heap_list[first]
