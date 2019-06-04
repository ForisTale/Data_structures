from min_heap import MinHeap


def test_min_heap():
    heap = MinHeap()
    heap.add(1)
    heap.add(2)

    value = heap.retrieve_min()
    assert value == 1


def test_add():
    heap = MinHeap()
    heap.add(2)
    heap.add(1)

    assert heap.heap_list[1] == 1


def test_heapify_up():
    heap = MinHeap()
    heap.heap_list = [None, 2, 3, 4, 1]
    heap.size = 4
    heap.heapify_up()

    assert heap.heap_list == [None, 1, 2, 4, 3]


def test_retrieve_min():
    heap = MinHeap()
    heap.heap_list = [None, 1, 2, 4, 3]
    heap.size = 2

    minimum = heap.retrieve_min()
    heap.size = 1
    assert minimum == 1
    assert heap.heap_list == [None, 2]

    heap.retrieve_min()
    assert heap.retrieve_min() == print("Error, heap is empty!")


def test_heapify_down():
    heap = MinHeap()
    heap.heap_list = [None, 4, 2, 3]
    heap.heapify_down()

    assert heap.heap_list == [None, 2, 4, 3]


def test_smaller_child():
    heap = MinHeap()
    heap.heap_list = [None, 3, 4, 5]
    smaller = heap.smaller_child(1)

    assert smaller == 2
