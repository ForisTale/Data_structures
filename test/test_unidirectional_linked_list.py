from unidirectional_linked_list import UnidirectionalLinkedList as ULinkedList
import pytest


def test_add_node():
    linked_list = ULinkedList()
    linked_list.add(1)
    assert linked_list.head_node.value == 1
    assert linked_list.head_node.get_next_node() is None

    linked_list.add(2)
    assert linked_list.head_node.get_next_node().value == 1


@pytest.mark.parametrize("value, result", [
    (3, 1),
    (2, 1),
])
def test_remove_node(value, result):
    linked_list = ULinkedList(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.remove_node(value)

    assert linked_list.get_head_node().get_next_node().get_value() == result


def test_get_error_message_when_try_remove_non_exist_value():
    linked_list = ULinkedList(1)

    assert linked_list.remove_node(5) == print("Error, can't find value in linked list to delete!")


@pytest.mark.parametrize("value_to_pop, result, next_node_value", [
    (2, 2, 3),
    (1, 1, 3),
])
def test_pop_node(value_to_pop, result, next_node_value):
    linked_list = ULinkedList(3)
    linked_list.add(2)
    linked_list.add(1)

    popped_node = linked_list.pop(value_to_pop)

    assert popped_node.get_value() == result
    assert linked_list.get_head_node().get_next_node().get_value() == next_node_value

    linked_list.pop(3)
    assert linked_list.get_head_node().get_next_node() is None

    result = linked_list.pop(4)
    assert result is None




