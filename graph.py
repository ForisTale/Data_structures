

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, value):
        self.graph_dict[value] = Vertex(value)

    def add_edge(self, from_vertex_value, to_vertex_value, weight=0):
        from_vertex = self.get_vertex(from_vertex_value)
        to_vertex = self.get_vertex(to_vertex_value)

        from_vertex.add_edge(to_vertex, weight)
        if not self.directed:
            to_vertex.add_edge(from_vertex, weight)

    def get_vertex(self, value):
        return self.graph_dict[value]

    def print(self):
        string = ""
        for key, item in self.graph_dict.items():
            string += f"Vertex {key} is connected to {item.get_edges()}.\n"
        print(string)


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __repr__(self):
        return self.value

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
