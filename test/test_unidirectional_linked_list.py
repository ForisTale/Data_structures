from unidirectional_linked_list import UnidirectionalLinkedList as ULinkedList
from node import Node
import pytest


def test_add_node():
    node = Node(1)
    linked_list = ULinkedList()
    linked_list.add_node(node)
    assert linked_list.head_node == node
    assert linked_list.head_node.get_link_node() is None

    other_node = Node(2)
    linked_list.add_node(other_node)
    assert linked_list.head_node.get_link_node() == node


@pytest.mark.parametrize("value, result", [
    (3, 1),
    (2, 1),
])
def test_remove_node(value, result):
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    linked_list = ULinkedList(node_1)
    linked_list.add_node(node_2)
    linked_list.add_node(node_3)

    linked_list.remove_node(value)

    assert linked_list.get_head_node().get_link_node().get_value() == result


def test_get_error_message_when_try_remove_non_exist_value():
    linked_list = ULinkedList(Node(1))

    assert linked_list.remove_node(5) == print("Error, can't find value in linked list to delete!")
