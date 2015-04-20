
class MinHeap(object):

    def __init__(self):
        self._heap = []
        self._heap_index = {}

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        return self

    def iter(self):
        return self

    @property
    def last_index(self):
        return len(self) - 1

    @property
    def root(self):
        return self._heap[0]

    def swap(self, i, j):
        # Swapping in Pythonic way
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

        value_i = self._heap[i][1]
        self._heap_index[value_i] = i

        value_j = self._heap[j][1]
        self._heap_index[value_j] = j

    def next(self):
        if not self._heap:
            raise StopIteration
            
        self.swap(0, self.last_index)
        popped = self._heap.pop(self.last_index)
        del self._heap_index[popped[1]]

        if self._heap:
            self.bubble_down()

        return popped

    def add(self, value, priority):
        self._heap.append((priority, value))
        self._heap_index[value] = self.last_index
        self.bubble_up()

    def index(self, value):
        return self._heap_index[value]

    def bubble_up(self, current_index=None):
        if current_index == None:
            current_index = self.last_index

        current = self._heap[current_index]
        parent_index, parent = self._get_parent(current_index)

        while parent and parent[0] > current[0]:
            self.swap(parent_index, current_index)

            current_index = parent_index
            parent_index, parent = self._get_parent(current_index)

    def bubble_down(self, current_index=None):
        if current_index == None:
            current_index = 0

        current = self._heap[current_index]
        child_index, child = self._get_lowest_priority_child(current_index)

        while child and child[0] < current[0]:
            self.swap(child_index, current_index)

            current_index = child_index
            child_index, child = self._get_lowest_priority_child(current_index)

    def _get_parent_index(self, index):
        if index == 0:
            return None

        if index % 2 == 0:
            parent_index = (index // 2) - 1
        else:
            parent_index = index // 2

        return parent_index 

    def _get_parent(self, index):
        parent_index = self._get_parent_index(index)

        if parent_index == None:
            return None, None

        return parent_index, self._heap[parent_index]

    def _get_children_index(self, index):
        left = index * 2 + 1
        if left > self.last_index:
            left = None

        right = index * 2 + 2
        if right > self.last_index:
            right = None

        return left, right

    def _get_children(self, index):
        left, right = self._get_children_index(index)
        if left:
            left_child = self._heap[left]
        else:
            left_child = None

        if right:
            right_child = self._heap[right]
        else:
            right_child = None

        return (left, left_child), (right, right_child)

    def _get_lowest_priority_child(self, index): 
        children = self._get_children(index)
        (left_index, left_child), (right_index, right_child) = children 

        if not any((left_child, right_child)):
            return None, None

        if not right_child or left_child[0] < right_child[0]:
            return left_index, left_child

        return right_index, right_child
