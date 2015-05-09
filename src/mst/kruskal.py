
from adt import UnionFind


def kruskal(g):
    edges = sorted(g.edges, key=lambda x: x.weight)

    components = UnionFind.from_graph(g)

    mst = []

    for edge in edges:
        if not components.connected(edge.v1, edge.v2):
            components.union(edge.v1, edge.v2)
            edge.mst = True
            mst.append(edge)

    return mst
