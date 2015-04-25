
from adt.unionfind import UnionFind


def kruskal(g):
    edges = sorted(g.edges, key=lambda x: x.weight)

    components = UnionFind(len(g.vertices))

    mst = []

    for edge in edges:
        v1_index = g.index(edge.v1)
        v2_index = g.index(edge.v2)

        if not components.connected(v1_index, v2_index):
            components.union(v1_index, v2_index)
            edge.mst = True
            mst.append(edge)

    return mst
