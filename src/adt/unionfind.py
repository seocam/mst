
from .graph import Graph


class UnionFind(Graph):

    def __init__(self):
        self._component_id = []
        self._component_size = []
        super(UnionFind, self).__init__()

    def add_vertice(self, x=None, y=None, vertice=None):
        super(UnionFind, self).add_vertice(x, y, vertice)
        self._component_id.append(len(self.vertices)-1)
        self._component_size.append(1)

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

        self.add_edge(p, q)

    def find(self, p):
        i = self.index(p)

        while i != self._component_id[i]:
            self._component_id[i] = self._component_id[self._component_id[i]]
            i = self._component_id[i]
        return i

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def groups(self):
        groups = {}
        for vertice in self.vertices:
            group_id = self.find(vertice)

            if group_id not in groups:
                groups[group_id] = []

            groups[group_id].append(vertice)
        return list(groups.values())
