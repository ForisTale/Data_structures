

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, value):
        self.graph_dict[value] = Vertex(value)

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex, weight)

    def get_vertex(self, value):
        return self.graph_dict[value]


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
