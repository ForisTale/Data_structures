from stack import Stack, StackIsFull, StackIsEmpty
import pytest


def test_push():
    stack = Stack()

    stack.push(1)
    stack.push(2)

    assert stack.top_item.value == 2
    assert stack.top_item.get_next_node().value == 1


def test_push_has_limit():
    stack = Stack(1)
    assert stack.limit == 1

    assert stack.has_space() is True
    stack.push(1)
    assert stack.has_space() is False

    with pytest.raises(StackIsFull):
        stack.push(2)


def test_peek(capsys):
    stack = Stack()
    assert stack.peek() is None
    captured = capsys.readouterr()
    assert captured.out == "Stack is empty!\n"

    stack.push(1)
    captured = capsys.readouterr()
    assert stack.peek() == 1
    assert captured.out == ""


def test_pop():
    stack = Stack()
    assert stack.is_empty() is True

    stack.push(1)
    stack.push(2)

    assert stack.is_empty() is False
    assert stack.pop() == 2
    assert stack.top_item.value == 1

    stack.pop()
    assert stack.is_empty() is True
    with pytest.raises(StackIsEmpty):
        stack.pop()
