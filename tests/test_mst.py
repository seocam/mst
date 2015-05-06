
import unittest

from adt.graph import Graph, Vertice, Edge
from mst import kruskal, prim


class TestMinimumSpanningTree(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        self.g.add_vertice(0, 0)
        self.g.add_vertice(3, 4)
        self.g.add_vertice(0, 4)
        self.g.add_vertice(3, 0)
        self.g.add_vertice(10, 40)

        self.mst = [
            Edge(Vertice(0, 0), Vertice(0, 4)),
            Edge(Vertice(3, 4), Vertice(0, 4)),
            Edge(Vertice(0, 0), Vertice(3, 0)),
            Edge(Vertice(3, 4), Vertice(10, 40)),
        ]

    def test_kruskal(self):
        mst = kruskal(self.g)
        self.assertEqual(sorted(mst), sorted(self.mst))

    def test_prim(self):
        mst = prim(self.g)
        self.assertEqual(sorted(mst), sorted(self.mst))
