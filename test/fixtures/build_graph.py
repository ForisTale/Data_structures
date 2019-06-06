from graph import Graph
import pytest


@pytest.fixture(params=[True, False])
def build_graph(request):
    graph = Graph(request.param)
    graph.add_vertex("vertex_1")
    graph.add_vertex("vertex_2")
    graph.add_vertex("vertex_3")
    graph.add_vertex("vertex_4")

    graph.add_edge("vertex_1", "vertex_3")
    graph.add_edge("vertex_3", "vertex_2", 1)
    yield graph

    for key, item in graph.graph_dict.items():
        item.edges = {}
