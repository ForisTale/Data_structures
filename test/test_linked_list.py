from linked_list import LinkedList
from node import Node


def test_default_values():
    linked_list = LinkedList()
    assert linked_list.head_node is None


def test_can_start_with_node():
    linked_list = LinkedList("test")
    assert linked_list.head_node.value == "test"


def test_has_get_head_node():
    linked_list = LinkedList()
    linked_list.get_head_node()


def test_can_iter_linked_list():
    node_2 = Node(2)
    node_3 = Node(3)

    linked_list = LinkedList(1)
    linked_list.get_head_node().set_next_node(node_2)
    linked_list.get_head_node().get_next_node().set_next_node(node_3)

    assert [num for num in linked_list] == [1, 2, 3]


def test_find_node_by_value():
    node_2 = Node(2)
    node_3 = Node(3)
    test_node = Node(2)

    linked_list = LinkedList(1)
    linked_list.get_head_node().set_next_node(node_2)
    linked_list.get_head_node().get_next_node().set_next_node(node_3)

    result = linked_list.find(2)

    assert node_2 is result
    assert test_node is not result

    result = linked_list.find(5)

    assert result is None
