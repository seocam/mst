
import unittest

from adt.graph import Vertice
from adt.unionfind import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        self.union_find = UnionFind()
        self.v = [
            Vertice(1, 0),
            Vertice(1, 1),
            Vertice(1, 2),
            Vertice(1, 3),
            Vertice(1, 4),
            Vertice(1, 5),
            Vertice(1, 6),
            Vertice(1, 7),
            Vertice(1, 8),
            Vertice(1, 9),
        ]
        for vertice in self.v:
            self.union_find.add_vertice(vertice.x, vertice.y)

    def test_union(self):
        self.assertNotEqual(self.union_find._component_id[2],
                            self.union_find._component_id[3])
        self.union_find.union(self.v[2], self.v[3])
        self.assertEqual(self.union_find._component_id[2],
                         self.union_find._component_id[3])

        # Already connected
        self.union_find.union(self.v[2], self.v[3])
        self.assertEqual(self.union_find._component_id[2],
                         self.union_find._component_id[3])

    def test_find(self):
        self.assertEqual(self.union_find.find(self.v[2]), 2)

    def test_connected(self):
        self.union_find.union(self.v[1], self.v[2])
        self.union_find.union(self.v[1], self.v[3])

        self.assertTrue(self.union_find.connected(self.v[2], self.v[3]))
        self.assertFalse(self.union_find.connected(self.v[3], self.v[4]))
        self.assertFalse(self.union_find.connected(self.v[4], self.v[5]))

        self.union_find.union(self.v[4], self.v[5])
        self.union_find.union(self.v[4], self.v[6])
        self.union_find.union(self.v[4], self.v[7])

        self.assertTrue(self.union_find.connected(self.v[4], self.v[5]))
        self.assertTrue(self.union_find.connected(self.v[4], self.v[7]))
        self.assertFalse(self.union_find.connected(self.v[2], self.v[7]))

        self.union_find.union(self.v[7], self.v[3])
        self.assertTrue(self.union_find.connected(self.v[2], self.v[7]))
