

class Graph:
    def __init__(self, directed=False):
        self.directed = directed


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
