
class UnionFind(list):

    def __init__(self, lenght):
        self._component_id = range(lenght)
        self._component_size = [1] * lenght

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
        while p != self._component_id[p]:
            self._component_id[p] = self._component_id[self._component_id[p]]
            p = self._component_id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)
