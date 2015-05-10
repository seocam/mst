
import unittest

from adt.graph import Graph, Vertice
from mst import kruskal, prim


class TestMinimumSpanningTree(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        self.g.add_connected_vertice(0, 0)
        self.g.add_connected_vertice(3, 4)
        self.g.add_connected_vertice(0, 4)
        self.g.add_connected_vertice(3, 0)
        self.g.add_connected_vertice(10, 40)

        self.mst = [[
            Vertice(0, 0),
            Vertice(0, 4),
            Vertice(3, 0),
            Vertice(3, 4),
            Vertice(10, 40),
        ]]

        self.three_groups = [
            [Vertice(0, 0), Vertice(3, 0)],
            [Vertice(3, 4), Vertice(0, 4)],
            [Vertice(10, 40)],
        ]

    def test_kruskal(self):
        mst = kruskal(self.g)
        self.assertGroupsEqual(mst, self.mst)

    def test_kruskal_groups(self):
        three_groups = kruskal(self.g, 3)
        self.assertGroupsEqual(three_groups, self.three_groups)

    def test_prim(self):
        mst = prim(self.g)
        self.assertGroupsEqual(mst, self.mst)

    def test_prim_groups(self):
        three_groups = prim(self.g, 3)
        self.assertGroupsEqual(three_groups, self.three_groups)

    def assertGroupsEqual(self, first, second, msg=None):
        try:
            key = lambda x: len(x)
            first.sort(key=key)
            second.sort(key=key)

            self.assertEqual(len(first), len(second))
            for i, group in enumerate(first):
                self.assertEqual(len(group), len(second[i]))
                for item in group:
                    self.assertIn(item, second[i])
        except AssertionError:
            msg = "Groups not equal\n\n{}\n{}".format(first, second)
            raise AssertionError(msg)
