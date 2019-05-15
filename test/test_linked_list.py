from linked_list import LinkedList
from node import Node


def test_default_values():
    linked_list = LinkedList()
    assert linked_list.head_node is None


def test_can_start_with_node():
    node = Node("test")
    linked_list = LinkedList(node)
    assert linked_list.head_node == node


def test_has_get_head_node():
    linked_list = LinkedList()
    linked_list.get_head_node()


def test_can_iter_linked_list():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    linked_list = LinkedList(node_1)
    linked_list.get_head_node().set_link_node(node_2)
    linked_list.get_head_node().get_link_node().set_link_node(node_3)

    assert [num for num in linked_list] == [1, 2, 3]
