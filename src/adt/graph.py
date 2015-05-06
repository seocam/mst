
from math import sqrt, log


class Vertice(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edges = []

    def __sub__(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)


class Edge(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.weight = v1 - v2
        self.mst = False

    def __repr__(self):
        return str(self)

    def to_graphviz(self):
        length = log(self.weight, 2) if self.weight > 2 else 1
        attrs = [
            'label={}'.format(self.weight),
            'len={0:.4f}'.format(length),
        ]

        if self.mst:
            attrs.append('color=red')
            attrs.append('penwidth=2.0')

        return '{}[{}]'.format(str(self), ','.join(attrs))

    def __str__(self):
        return '"{}" -- "{}"'.format(self.v1, self.v2)

    def __eq__(self, other):
        return self.v1, self.v2 == other.v1, other.v2


class Graph(object):

    def __init__(self):
        self.edges = []
        self.vertices = []
        self.vertices_index = {}

    def add_vertice(self, x, y):
        new_vertice = Vertice(x, y)

        for vertice in self.vertices:
            edge = Edge(vertice, new_vertice)
            self.edges.append(edge)
            new_vertice.edges.append(edge)
            vertice.edges.append(edge)

        self.vertices_index[new_vertice] = len(self.vertices)
        self.vertices.append(new_vertice)

    def index(self, vertice):
        return self.vertices_index[vertice]

    def to_graphviz(self):
        edges_str = []
        for edge in self.edges:
            edges_str.append(edge.to_graphviz())
        return 'graph { ' + ';\n'.join(edges_str) + '; }'
