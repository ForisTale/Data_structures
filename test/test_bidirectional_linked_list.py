from bidirectional_linked_list import BidirectionalLinkedList as BLinkedList
from bidirectional_linked_list import BidirectionalNode as BNode


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


def test_bidirectional_node_has_basic_methods():
    node = BNode(1)
    node.get_value()
    node.get_next_node()
    node.get_prev_node()
    node.set_next_node(None)
    node.set_prev_node(None)
