
from .graph import Graph


class UnionFind(Graph):

    def __init__(self):
        self._component_id = []
        self._component_size = []
        super(UnionFind, self).__init__()

    def add_vertice(self, x, y):
        self._component_id.append(len(self.vertices))
        self._component_size.append(1)
        super(UnionFind, self).add_vertice(x, y)

    @classmethod
    def from_graph(cls, graph):
        unionfind = cls()
        for vertice in graph.vertices:
            unionfind.add_vertice(vertice.x, vertice.y)
        return unionfind

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)

        if pid == qid:
            return

        size_p = self._component_size[pid]
        size_q = self._component_size[qid]

        if size_q >= size_p:
            self._component_id[qid] = pid
            self._component_size[pid] = size_p + size_q
        else:
            self._component_id[pid] = qid
            self._component_size[qid] = size_p + size_q

    def find(self, p):
        i = self.index(p)

        while i != self._component_id[i]:
            self._component_id[i] = self._component_id[self._component_id[i]]
            i = self._component_id[i]
        return i

    def connected(self, p, q):
        return self.find(p) == self.find(q)
