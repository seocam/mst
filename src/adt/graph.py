
from math import sqrt


class Vertice(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Edge(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.weight = v1 - v2
        self.color = None

    def __str__(self):
        return '"{}" -- "{}": {}'.format(self.v1, self.v2, self.weight)

    def __eq__(self, other):
        return self.v1, self.v2 == other.v1, other.v2


class Graph(object):

    def __init__(self):
        self.edges = []
        self.vertices = []

    def add_vertice(self, x, y):
        new_vertice = Vertice(x, y)

        for vertice in self.vertices:
            edge = Edge(vertice, new_vertice)
            self.edges.append(edge)

        self.vertices.append(new_vertice)
