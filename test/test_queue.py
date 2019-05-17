from my_queue import Queue, QueueIsEmpty, QueueIsFull
from node import Node
import pytest


def test_enqueue():
    queue = Queue()
    node_1 = Node(1)
    node_2 = Node(2)

    queue.enqueue(node_1)
    queue.enqueue(node_2)

    assert queue.head == node_2
    assert queue.tail == node_1


def test_has_limit():
    queue = Queue(1)
    assert queue.has_space() is True
    assert queue.limit == 1

    node_1 = Node(1)
    node_2 = Node(2)
    queue.enqueue(node_1)
    assert queue.has_space() is False
    with pytest.raises(QueueIsFull):
        queue.enqueue(node_2)


def test_get_size():
    queue = Queue()
    node = Node(1)
    assert queue.get_size() == 0
    queue.enqueue(node)
    assert queue.get_size() == 1
    queue.dequeue()
    assert queue.get_size() == 0


def test_peek():
    queue = Queue()
    node = Node(1)
    queue.enqueue(node)

    assert queue.peek() == 1


def test_dequeue():
    queue = Queue()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    queue.enqueue(node_1)
    queue.enqueue(node_2)
    queue.enqueue(node_3)

    assert queue.dequeue() == 1
    assert queue.head == node_3
    assert queue.tail == node_2
    queue.dequeue()
    assert queue.dequeue() == 3
    assert queue.head is None
    assert queue.tail is None


def test_is_empty():
    queue = Queue()
    assert queue.is_empty() is True

    node = Node(1)
    queue.enqueue(node)
    assert queue.is_empty() is False


def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises(QueueIsEmpty):
        queue.dequeue()
