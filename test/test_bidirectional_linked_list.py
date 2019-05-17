from bidirectional_linked_list import BidirectionalLinkedList as BLinkedList
from bidirectional_linked_list import BidirectionalNode as BNode
import pytest


def test_add_node():
    node_1 = BNode(1)
    node_2 = BNode(2)
    node_3 = BNode(3)

    linked_list = BLinkedList(node_1)
    linked_list.add_node(node_2)
    linked_list.add_node(node_3)
    second_node = linked_list.get_head_node().get_next_node()

    assert second_node.get_next_node() == node_1
    assert second_node.get_prev_node() == node_3


@pytest.mark.parametrize("value, result, prev_node, next_node", [
    (3, 1, "node_2", "None"),
    (2, 1, "node_3", "None"),
])
def test_remove_node(value, result, prev_node, next_node):
    node_1 = BNode(1)
    node_2 = BNode(2)
    node_3 = BNode(3)

    linked_list = BLinkedList(node_1)
    linked_list.add_node(node_2)
    linked_list.add_node(node_3)

    linked_list.remove_node(value)

    assert linked_list.get_head_node().get_next_node().get_value() == result
    assert linked_list.get_head_node().get_next_node().get_prev_node() == eval(prev_node)
    assert linked_list.get_head_node().get_next_node().get_next_node() == eval(next_node)


def test_get_error_message_when_try_remove_non_exist_value():
    linked_list = BLinkedList(BNode(1))

    assert linked_list.remove_node(5) == print("Error, can't find value in linked list to delete!")


def test_bidirectional_node_has_basic_methods():
    node = BNode(1)
    node.get_value()
    node.get_next_node()
    node.get_prev_node()
    node.set_next_node(None)
    node.set_prev_node(None)
