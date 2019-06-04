

class Graph:
    def __init__(self, directed=False):
        self.directed = directed

    def add_vertex(self, vertex):
        pass

    def add_edge(self, from_vertex, to_vertex, weight=0):
        pass

    def has_path(self, start_vertex, end_vertex):
        pass


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
