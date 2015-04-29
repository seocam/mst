
import unittest

from adt.graph import Graph, Vertice, Edge

from nose.tools import assert_equal

assert_equal.__self__.maxDiff = None


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

    def test_repr(self):
        vertice = Vertice(9, 1)
        self.assertEqual(str(vertice), repr(vertice))


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

    def test_repr(self):
        self.assertEqual(str(self.edge), repr(self.edge))


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

    def test_repr(self):
        self.graph.add_vertice(3, 4)
        self.assertEqual(str(self.graph), repr(self.graph))

    def test_graphviz(self):
        self.graph.add_vertice(0, 0)
        self.graph.add_vertice(3, 4)
        self.graph.add_vertice(0, 4)
        self.graph.edges[-1].mst = True
        self.graph.add_vertice(3, 0)
        graphviz_res = """
graph { "(0, 0)" -- "(3, 4)"[label=5.0,len=2.32192809489];
"(0, 0)" -- "(0, 4)"[label=4.0,len=2.0];
"(3, 4)" -- "(0, 4)"[label=3.0,len=1.58496250072,color=red,penwidth=2.0];
"(0, 0)" -- "(3, 0)"[label=3.0,len=1.58496250072];
"(3, 4)" -- "(3, 0)"[label=4.0,len=2.0];
"(0, 4)" -- "(3, 0)"[label=5.0,len=2.32192809489]; }""".strip()

        print('-' * 80)
        print(graphviz_res)
        print('-' * 80)
        print(self.graph.to_graphviz())
        print('-' * 80)

        assert_equal(self.graph.to_graphviz(), graphviz_res)

    def test_vertice_index(self):
        self.graph.add_vertice(0, 0)
        vertice = self.graph.vertices[-1]
        self.assertEqual(self.graph.index(vertice), 0)

        self.graph.add_vertice(3, 4)
        vertice = self.graph.vertices[-1]
        self.assertEqual(self.graph.index(vertice), 1)

        self.graph.add_vertice(0, 4)
        vertice = self.graph.vertices[-1]
        self.assertEqual(self.graph.index(vertice), 2)
