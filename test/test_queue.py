from my_queue import Queue, QueueIsEmpty, QueueIsFull
import pytest


def test_enqueue():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.head.value == 2
    assert queue.tail.value == 1


def test_has_limit():
    queue = Queue(1)
    assert queue.has_space() is True
    assert queue.limit == 1

    queue.enqueue(1)
    assert queue.has_space() is False
    with pytest.raises(QueueIsFull):
        queue.enqueue(2)


def test_get_size():
    queue = Queue()
    assert queue.get_size() == 0
    queue.enqueue(1)
    assert queue.get_size() == 1
    queue.dequeue()
    assert queue.get_size() == 0


def test_peek():
    queue = Queue()
    queue.enqueue(1)

    assert queue.peek() == 1


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.head.value == 3
    assert queue.tail.value == 2
    queue.dequeue()
    assert queue.dequeue() == 3
    assert queue.head is None
    assert queue.tail is None


def test_is_empty():
    queue = Queue()
    assert queue.is_empty() is True

    queue.enqueue(1)
    assert queue.is_empty() is False


def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises(QueueIsEmpty):
        queue.dequeue()
