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
    yield graph

    vertex_1.edges = {}
    vertex_2.edges = {}
    vertex_3.edges = {}
    vertex_4.edges = {}


def test_is_directed(build_graph):
    graph = build_graph

    if graph.directed is False:
        cases_for_directed = {vertex_1: 0, vertex_2: 1}
    else:
        cases_for_directed = {vertex_2: 1}

    assert vertex_3.edges == cases_for_directed


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
