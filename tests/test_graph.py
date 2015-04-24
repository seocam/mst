
import unittest

from adt.graph import Graph, Vertice, Edge


class TestVertice(unittest.TestCase):

    def test_init(self):
        vertice = Vertice(10, 23)
        self.assertEqual(vertice.x, 10)
        self.assertEqual(vertice.y, 23)

    def test_euclidian_distance(self):
        v1 = Vertice(0, 0)
        v2 = Vertice(3, 4)
        self.assertEqual(v1-v2, 5)

    def test_str(self):
        vertice = Vertice(9, 1)
        self.assertEqual('(9, 1)', str(vertice))


class TestEdge(unittest.TestCase):

    def setUp(self):
        self.v1 = Vertice(0, 0)
        self.v2 = Vertice(3, 4)
        self.edge = Edge(self.v1, self.v2)

    def test_init(self):
        self.assertEqual(self.edge.v1, self.v1)
        self.assertEqual(self.edge.v2, self.v2)
        self.assertEqual(self.edge.weight, 5)

    def test_str(self):
        self.assertEqual('"(0, 0)" -- "(3, 4)"', str(self.edge))


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_vertice(self):
        vertices = []
        edges = []
        self.assertEqual(self.graph.edges, edges)
        self.assertEqual(self.graph.vertices, vertices)

        self.graph.add_vertice(0, 0)
        vertices.append(Vertice(0, 0))
        self.assertEqual(self.graph.edges, edges)
        self.assertEqual(self.graph.vertices, vertices)

        self.graph.add_vertice(3, 4)
        vertices.append(Vertice(3, 4))
        edges.append(Edge(vertices[0], vertices[1]))
        self.assertEqual(self.graph.edges, edges)

        self.graph.add_vertice(0, 4)
        vertices.append(Vertice(0, 4))
        edges.append(Edge(vertices[0], vertices[1]))
        edges.append(Edge(vertices[0], vertices[2]))
        self.assertEqual(self.graph.edges, edges)
        self.assertEqual(self.graph.vertices, vertices)
