from node import Node


def test_node_none_default_link():
    node = Node("test")

    assert node.link_node is None


def test_node_has_get_value_set_link_node_get_link_node():
    node = Node("test")
    other_node = Node("test")
    node.get_value()
    node.set_link_node(other_node)
    node.get_link_node()
