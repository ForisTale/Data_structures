from bidirectional_linked_list import BidirectionalLinkedList as BLinkedList
from bidirectional_linked_list import BidirectionalNode as BNode
import pytest


def test_add_node():

    linked_list = BLinkedList(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    second_node = linked_list.get_head_node().get_next_node()

    assert second_node.get_next_node().value == 1
    assert second_node.get_prev_node().value == 3


@pytest.mark.parametrize("value, result, prev_node, next_node", [
    (3, 1, "Node with value: 2", "None"),
    (2, 1, "Node with value: 3", "None"),
])
def test_remove_node(value, result, prev_node, next_node):

    linked_list = BLinkedList(1)
    linked_list.add_node(2)
    linked_list.add_node(3)

    linked_list.remove_node(value)

    assert linked_list.get_head_node().get_next_node().get_value() == result
    assert str(linked_list.get_head_node().get_next_node().get_prev_node()) == prev_node
    assert str(linked_list.get_head_node().get_next_node().get_next_node()) == next_node


def test_get_error_message_when_try_remove_non_exist_value():
    linked_list = BLinkedList(1)

    assert linked_list.remove_node(5) == print("Error, can't find value in linked list to delete!")


def test_bidirectional_node_has_basic_methods():
    node = BNode(1)
    node.get_value()
    node.get_next_node()
    node.get_prev_node()
    node.set_next_node(None)
    node.set_prev_node(None)
