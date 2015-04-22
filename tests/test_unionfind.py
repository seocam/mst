
import unittest

from ..adt.unionfind import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        self.union_find = UnionFind(10)

    def test_union(self):
        self.assertNotEqual(self.union_find._component_id[2],
                            self.union_find._component_id[3])
        self.union_find.union(2, 3)
        self.assertEqual(self.union_find._component_id[2],
                         self.union_find._component_id[3])

        # Already connected
        self.union_find.union(2, 3)
        self.assertEqual(self.union_find._component_id[2],
                         self.union_find._component_id[3])

    def test_find(self):
        self.assertEqual(self.union_find.find(2), 2)

    def test_connected(self):
        self.union_find.union(1, 2)
        self.union_find.union(1, 3)

        self.assertTrue(self.union_find.connected(2, 3))
        self.assertFalse(self.union_find.connected(3, 4))
        self.assertFalse(self.union_find.connected(4, 5))

        self.union_find.union(4, 5)
        self.union_find.union(4, 6)
        self.union_find.union(4, 7)

        self.assertTrue(self.union_find.connected(4, 5))
        self.assertTrue(self.union_find.connected(4, 7))
        self.assertFalse(self.union_find.connected(2, 7))

        self.union_find.union(7, 3)
        self.assertTrue(self.union_find.connected(2, 7))
