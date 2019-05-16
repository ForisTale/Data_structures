from stack import Stack, StackIsFull, StackIsEmpty
from node import Node
import pytest


def test_push():
    node_1 = Node(1)
    node_2 = Node(2)
    stack = Stack()

    stack.push(node_1)
    stack.push(node_2)

    assert stack.top_item == node_2
    assert stack.top_item.get_link_node() == node_1


def test_push_has_limit():
    stack = Stack(1)
    assert stack.limit == 1

    node_1 = Node(1)
    node_2 = Node(2)

    assert stack.has_space() is True
    stack.push(node_1)
    assert stack.has_space() is False

    with pytest.raises(StackIsFull):
        stack.push(node_2)


def test_peek():
    stack = Stack()
    assert stack.peek() == "Stack is empty!"
    node = Node(1)
    stack.push(node)
    assert stack.peek() == 1


def test_pop():
    stack = Stack()
    assert stack.is_empty() is True

    node_1 = Node(1)
    node_2 = Node(2)
    stack.push(node_1)
    stack.push(node_2)

    assert stack.is_empty() is False
    assert stack.pop() == 2
    assert stack.top_item == node_1

    stack.pop()
    assert stack.is_empty() is True
    with pytest.raises(StackIsEmpty):
        stack.pop()
