from graph import Graph, Vertex


def test_show_path_in_bidirectional_graph():
    graph = Graph()
    vertex_1 = Vertex(1)
    vertex_2 = Vertex(2)
    vertex_3 = Vertex(3)

    graph.add_vertex(vertex_1)
    graph.add_vertex(vertex_2)
    graph.add_vertex(vertex_3)

    graph.add_edge(vertex_1, vertex_3)
    graph.add_edge(vertex_3, vertex_2)

    graph.show_path(vertex_1, vertex_2)


def test_show_path_in_directional_graph():
    pass


def test_vertex():
    vertex_1 = Vertex(1)
    vertex_2 = Vertex(2)

    assert vertex_1.value == 1

    assert vertex_1.get_edges() == []
    vertex_1.add_edge(vertex_2)
    assert vertex_1.edges == {vertex_2: 0}
    assert vertex_1.get_edges() == [vertex_2]

    vertex_1.edges = {}
    vertex_1.add_edge(vertex_2, 1)
    assert vertex_1.edges == {vertex_2: 1}
