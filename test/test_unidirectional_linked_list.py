from unidirectional_linked_list import UnidirectionalLinkedList as ULinkedList
from node import Node


def test_default_values():
    linked_list = ULinkedList()
    assert linked_list.head_node is None


def test_can_start_with_node():
    node = Node("test")
    linked_list = ULinkedList(node)
    assert linked_list.head_node == node


def test_add_node():
    node = Node(1)
    linked_list = ULinkedList()
    linked_list.add_node(node)
    assert linked_list.head_node == node
    assert linked_list.head_node.get_link_node() is None

    other_node = Node(2)
    linked_list.add_node(other_node)
    assert linked_list.head_node.get_link_node() == node


def test_has_get_head_node():
    linked_list = ULinkedList()
    linked_list.get_head_node()


def test_can_iter_linked_list():
    node_1 = 1
    node_2 = 2
    node_3 = 3

    linked_list = ULinkedList(node_1)
    linked_list.add_node(node_2)
    linked_list.add_node(node_3)

    assert [num for num in linked_list] == [3, 2, 1]


def test_remove_node():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    linked_list = ULinkedList(node_1)
    linked_list.add_node(node_2)
    linked_list.add_node(node_3)

    assert linked_list.remove_node(5) == print("Error, can't find value to delete!")
    linked_list.remove_node(2)

    assert linked_list.get_head_node() == 3
    assert linked_list.get_head_node().get_link_node().get_value() == 1
