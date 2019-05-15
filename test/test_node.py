from node import Node
import pytest


def test_node_none_default_link():
    node = Node("test")

    assert node.link_node is None


def test_node_has_get_value_set_link_node_get_link_node():
    node = Node("test")
    other_node = Node("test")
    node.get_value()
    node.set_link_node(other_node)
    node.get_link_node()


@pytest.mark.parametrize("value, result", [
    ("test", "Node with value: test"),
    ([], "Node with value: []"),
    (Node(1), "Node with value: Node with value: 1"),
])
def test_node_repr(value, result):
    node = Node(value)
    assert str(node) == result
