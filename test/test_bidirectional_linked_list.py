from bidirectional_linked_list import BidirectionalLinkedList as BLinkedList
from bidirectional_linked_list import BidirectionalNode as BNode
import pytest


def test_add_node():

    linked_list = BLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)
    second_node = linked_list.get_head_node().get_next_node()

    assert second_node.get_next_node().value == 1
    assert second_node.get_prev_node().value == 3


@pytest.mark.parametrize("value, result, prev_node, next_node", [
    (3, 1, "Node with value: 2", "None"),
    (2, 1, "Node with value: 3", "None"),
])
def test_remove_node(value, result, prev_node, next_node):

    linked_list = BLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.remove_node(value)

    assert linked_list.get_head_node().get_next_node().get_value() == result
    assert str(linked_list.get_head_node().get_next_node().get_prev_node()) == prev_node
    assert str(linked_list.get_head_node().get_next_node().get_next_node()) == next_node


def test_remove_all_items():
    linked_list = BLinkedList(1)
    linked_list.remove_node(1)

    assert linked_list.head_node is None


def test_get_error_message_when_try_remove_non_exist_value():
    linked_list = BLinkedList(1)

    assert linked_list.remove_node(5) == print("Error, can't find value in linked list to delete!")

    linked_list.remove_node(1)
    assert linked_list.remove_node(1) == print("Error, can't find value in linked list to delete!")


@pytest.mark.parametrize("value_to_pop, result, value_list", [
    (2, 2, [1, 3]),
    (1, 1, [2, 3]),
])
def test_pop_node(value_to_pop, result, value_list):
    linked_list = BLinkedList(3)
    linked_list.add(2)
    linked_list.add(1)

    popped_node = linked_list.pop(value_to_pop)
    ll_value_list = linked_list.traverse()

    assert popped_node.get_value() == result
    assert ll_value_list == value_list

    backward_traverse = backward(linked_list, ll_value_list[-1])
    value_list.reverse()

    assert backward_traverse == value_list

    linked_list.pop(3)
    assert linked_list.get_head_node().get_next_node() is None

    result = linked_list.pop(4)
    assert result is None


def test_bidirectional_node_has_basic_methods():
    node = BNode(1)
    node.get_value()
    node.get_next_node()
    node.get_prev_node()
    node.set_next_node(None)
    node.set_prev_node(None)


def backward(linked_list, last_value):
    last_node = linked_list.find(last_value)
    reverse_value_list = []
    while last_node:
        reverse_value_list.append(last_node.get_value())
        last_node = last_node.get_prev_node()
    return reverse_value_list


def test_backward():
    linked_list = BLinkedList(3)
    linked_list.add(2)
    linked_list.add(1)

    value_list = backward(linked_list, 3)
    assert value_list == [3, 2, 1]
