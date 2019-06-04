from linked_list import LinkedList
from node import Node
import pytest


@pytest.fixture()
def build_linked_list():
    node_2 = Node(2)
    node_3 = Node(3)

    linked_list = LinkedList(1)
    linked_list.get_head_node().set_next_node(node_2)
    linked_list.get_head_node().get_next_node().set_next_node(node_3)

    return linked_list


def test_default_values():
    linked_list = LinkedList()
    assert linked_list.head_node is None


def test_can_start_with_node():
    linked_list = LinkedList("test")
    assert linked_list.head_node.value == "test"


def test_can_iter_linked_list(build_linked_list):
    linked_list = build_linked_list
    assert [num for num in linked_list] == [1, 2, 3]


def test_find_node_by_value(build_linked_list):
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


def test_traverse(build_linked_list):
    linked_list = build_linked_list

    ll_list = linked_list.traverse()
    assert ll_list == [1, 2, 3]

    empty_ll = LinkedList()
    empty_list = empty_ll.traverse()
    assert empty_list == []
