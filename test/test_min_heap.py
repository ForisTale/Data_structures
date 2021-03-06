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


def test_retrieve_min(capsys):
    heap = MinHeap()
    heap.heap_list = [None, 1, 2, 4, 3]
    heap.size = 4

    minimum = heap.retrieve_min()
    assert heap.size == 3
    assert minimum == 1
    assert heap.heap_list == [None, 2, 3, 4]

    heap.retrieve_min()
    heap.retrieve_min()
    heap.retrieve_min()
    assert heap.retrieve_min() is None
    captured = capsys.readouterr()
    assert captured.out == "Error, heap is empty!\n"


def test_heapify_down():
    heap = MinHeap()
    heap.heap_list = [None, 4, 2, 3]
    heap.size = 3
    heap.heapify_down()

    assert heap.heap_list == [None, 2, 4, 3]


def test_smaller_child():
    heap = MinHeap()
    heap.heap_list = [None, 3, 4, 5]
    heap.size = 3
    smaller_1 = heap.get_smaller_child(1)
    heap.heap_list = [None, 3, 5, 4]
    smaller_2 = heap.get_smaller_child(1)

    assert smaller_1 == 2
    assert smaller_2 == 3

    heap.heap_list = [None, 3, 4]
    heap.size = 2
    smaller = heap.get_smaller_child(1)

    assert smaller == 2


def test_swap():
    heap = MinHeap()
    heap.heap_list = [None, 3, 4]
    heap.swap(1, 2)

    assert heap.heap_list == [None, 4, 3]


def test_has_child():
    heap = MinHeap()
    heap.heap_list = [None, 3, 4]
    heap.size = 2
    for_num_3 = heap.has_child(1)
    for_num_4 = heap.has_child(2)

    assert for_num_3 is True
    assert for_num_4 is False
