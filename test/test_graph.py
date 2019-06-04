from graph import Graph, Vertex
import pytest


vertex_1 = Vertex(1)
vertex_2 = Vertex(2)
vertex_3 = Vertex(3)
vertex_4 = Vertex(4)


@pytest.fixture(params=[True, False])
def build_graph(request):
    graph = Graph(request.param)
    graph.add_vertex(vertex_1)
    graph.add_vertex(vertex_2)
    graph.add_vertex(vertex_3)
    graph.add_vertex(vertex_4)

    graph.add_edge(vertex_1, vertex_3)
    graph.add_edge(vertex_3, vertex_2, 1)
    return graph


def test_has_path(build_graph):
    graph = build_graph

    if graph.directed is False:
        cases_for_directed = [{vertex_1: 0, vertex_2: 1}, True]
    else:
        cases_for_directed = [{vertex_2: 1}, False]

    assert vertex_3.edges == cases_for_directed[0]

    assert graph.has_path(vertex_1, vertex_2) is True
    assert graph.has_path(vertex_2, vertex_1) is cases_for_directed[1]
    assert graph.has_path(vertex_1, vertex_4) is False


def test_add_vertex(build_graph):
    graph = build_graph
    assert graph.graph_dict == {1: vertex_1, 2: vertex_2, 3: vertex_3, 4: vertex_4}


def test_vertex():

    assert vertex_1.value == 1

    assert vertex_1.get_edges() == []
    vertex_1.add_edge(vertex_2)
    assert vertex_1.edges == {vertex_2: 0}
    assert vertex_1.get_edges() == [vertex_2]

    vertex_1.edges = {}
    vertex_1.add_edge(vertex_2, 1)
    assert vertex_1.edges == {vertex_2: 1}
