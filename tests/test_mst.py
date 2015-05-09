
import unittest

from adt.graph import Graph, Vertice, Edge
from mst import kruskal, prim, split_in_groups


class TestMinimumSpanningTree(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        self.g.add_connected_vertice(0, 0)
        self.g.add_connected_vertice(3, 4)
        self.g.add_connected_vertice(0, 4)
        self.g.add_connected_vertice(3, 0)
        self.g.add_connected_vertice(10, 40)

        self.mst2 = [
            Edge(Vertice(0, 0), Vertice(0, 4)),
            Edge(Vertice(3, 4), Vertice(0, 4)),
            Edge(Vertice(0, 0), Vertice(3, 0)),
            Edge(Vertice(3, 4), Vertice(10, 40)),
        ]

        self.mst = [[
            Vertice(0, 0),
            Vertice(0, 4),
            Vertice(3, 0),
            Vertice(3, 4),
            Vertice(10, 40),
        ]]

    def test_kruskal(self):
        mst = kruskal(self.g)
        self.assertCountEqual(mst, self.mst)

    def test_kruskal_groups(self):
        mst = prim(self.g)
        groups_1 = split_in_groups(mst, 3)
        groups_2 = kruskal(self.g, 3)
        self.assertCountEqual(groups_1, groups_2)

    def test_prim(self):
        mst = prim(self.g)
        self.assertCountEqual(mst, self.mst)

    def test_grouping(self):
        groups = split_in_groups(self.mst2)
        self.assertEqual(len(groups), 2)
        groups.sort(key=lambda x: len(x))
        self.assertIn(Vertice(10, 40), groups[0])
        self.assertIn(Vertice(0, 0), groups[1])
        self.assertIn(Vertice(3, 4), groups[1])
        self.assertIn(Vertice(0, 4), groups[1])
        self.assertIn(Vertice(3, 0), groups[1])

        groups = split_in_groups(self.mst2, 3)
        self.assertEqual(len(groups), 3)
        groups.sort(key=lambda x: len(x))
        self.assertIn(Vertice(10, 40), groups[0])
        self.assertIn(Vertice(0, 0), groups[1])
        self.assertIn(Vertice(3, 0), groups[1])
        self.assertIn(Vertice(3, 4), groups[2])
        self.assertIn(Vertice(0, 4), groups[2])

    def assertCountEqual(self, first, second, msg=None):
        try:
            super(TestMinimumSpanningTree, self).assertCountEqual(first,
                                                                  second, msg)
        except AttributeError:
            key = lambda x: len(x)
            first.sort(key=key)
            second.sort(key=key)

            for i, group in enumerate(first):
                self.assertEqual(len(group), len(second[i]))
                for item in group:
                    self.assertIn(item, second[i])
