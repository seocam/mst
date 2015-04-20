
import unittest

from heap import MinHeap


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()

    def test_get_parent_index(self):
        self.assertEqual(self.heap._get_parent_index(0), None)
        self.assertEqual(self.heap._get_parent_index(1), 0)
        self.assertEqual(self.heap._get_parent_index(2), 0)
        self.assertEqual(self.heap._get_parent_index(3), 1)
        self.assertEqual(self.heap._get_parent_index(4), 1)
        self.assertEqual(self.heap._get_parent_index(5), 2)
        self.assertEqual(self.heap._get_parent_index(6), 2)
        self.assertEqual(self.heap._get_parent_index(7), 3)
        self.assertEqual(self.heap._get_parent_index(8), 3)
        self.assertEqual(self.heap._get_parent_index(9), 4)
        self.assertEqual(self.heap._get_parent_index(100), 49)
        self.assertEqual(self.heap._get_parent_index(101), 50)

    def test_add(self):
        self.heap.add(value=10, priority=10)
        self.assertEqual(self.heap.root, (10, 10))
        self.heap.add(value=20, priority=20)
        self.assertEqual(self.heap.root, (10, 10))
        self.heap.add(value=5, priority=5)
        self.assertEqual(self.heap.root, (5, 5))
        self.heap.add(value=7, priority=7)
        self.assertEqual(self.heap.root, (5, 5))
        self.heap.add(value=3, priority=3)
        self.assertEqual(self.heap.root, (3, 3))

        heap = [(3, 3), (5, 5), (10, 10), (20, 20), (7, 7)]
        self.assertEqual(self.heap._heap, heap)

    def test_len(self):
        self.assertEqual(len(self.heap), 0)
        self.heap.add(value=10, priority=10)
        self.assertEqual(len(self.heap), 1)
        self.heap.add(value=15, priority=15)
        self.heap.add(value=20, priority=20)
        self.heap.add(value=25, priority=25)
        self.assertEqual(len(self.heap), 4)

    def test_get_children_index(self):
        self.assertEqual(self.heap._get_children_index(0), (None, None))
        self.heap.add(value=10, priority=10)
        self.assertEqual(self.heap._get_children_index(0), (None, None))
        self.heap.add(value=15, priority=15)
        self.assertEqual(self.heap._get_children_index(0), (1, None))
        self.heap.add(value=20, priority=20)
        self.assertEqual(self.heap._get_children_index(0), (1, 2))
        for i in range(21):
            self.heap.add(value=i, priority=i)

        self.assertEqual(self.heap._get_children_index(5), (11, 12))
        self.assertEqual(self.heap._get_children_index(11), (23, None))

    def test_next(self):
        self.heap.add(value=10, priority=10)
        self.heap.add(value=20, priority=20)
        self.heap.add(value=5, priority=5)
        self.heap.add(value=7, priority=7)
        self.heap.add(value=3, priority=3)

        self.assertEqual(self.heap.next(), (3, 3))
        self.assertEqual(self.heap.root, (5, 5))
        self.assertEqual(self.heap.next(), (5, 5))
        self.assertEqual(self.heap.root, (7, 7))
        self.assertEqual(self.heap.next(), (7, 7))
        self.assertEqual(self.heap.root, (10, 10))
        self.heap.next()
        self.assertEqual(self.heap.root, (20, 20))
        self.heap.next()

        with self.assertRaises(StopIteration):
            self.heap.next()

    def test_next_with_right_lowest(self):
        self.heap.add(value=10, priority=10)
        self.heap.add(value=5, priority=5)
        self.heap.add(value=3, priority=3)
        self.heap.add(value=15, priority=15)

        self.assertEqual(self.heap.next(), (3, 3))
        self.assertEqual(self.heap.root, (5, 5))

    def test_index(self):
        self.heap.add(value=10, priority=10)
        self.assertEqual(self.heap.index(10), 0)

        self.heap.add(value=20, priority=20)
        self.assertEqual(self.heap.index(20), 1)

        self.heap.add(value=5, priority=5)
        self.assertEqual(self.heap.index(5), 0)

        self.heap.add(value=7, priority=7)
        self.heap.add(value=3, priority=3)

        heap = [(3, 3), (5, 5), (10, 10), (20, 20), (7, 7)]
        for (i, (p, value)) in enumerate(self.heap._heap):
            self.assertEqual(self.heap.index(value), i)

    def test_decrease_priority(self):
        self.heap.add(value=10, priority=10)
        self.heap.add(value=5, priority=5)
        self.heap.add(value=3, priority=3)
        self.heap.add(value=15, priority=15)

        self.heap.update(15, 1)
        heap = [(1, 15), (3, 3), (5, 5), (10, 10)]
        self.assertEqual(self.heap._heap, heap)

    def test_increase_priority(self):
        self.heap.add(value=10, priority=10)
        self.heap.add(value=5, priority=5)
        self.heap.add(value=3, priority=3)
        self.heap.add(value=15, priority=15)

        self.heap.update(3, 12)
        heap = [(5, 5), (10, 10), (12, 3), (15, 15)]
        self.assertEqual(self.heap._heap, heap)

        self.heap.add(value=20, priority=20)
        self.heap.update(5, 25)
        heap = [(10, 10), (15, 15), (12, 3), (25, 5), (20, 20)]
        self.assertEqual(self.heap._heap, heap)
