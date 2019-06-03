from min_heap import MinHeap


def test_min_heap():
    heap = MinHeap()
    heap.add(1)
    heap.add(2)

    value = heap.retrieve()
    assert value == 1


def test_add():
    heap = MinHeap()
    heap.add(2)
    heap.add(1)

    assert heap.heap[0] == 1


def test_heapify_up():
    heap = MinHeap()
    heap.heap = [None, 2, 3, 4, 1]
    heap.heapify_up()

    assert heap.heap == [None, 1, 2, 3, 4]
