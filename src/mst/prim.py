
from adt import MinHeap

INFINITY = 2 ** 64


def prim(g):
    visited = {}

    edges = {}
    costs = MinHeap()

    for vertice in g.vertices:
        costs[vertice] = INFINITY
        edges[vertice] = None

    mst = []

    for p, vertice in costs:
        visited[vertice] = True
        if edges[vertice] is not None:
            mst.append(edges[vertice])
            edges[vertice].mst = True

        for edge in vertice.edges:
            v = edge.v1 if edge.v1 != vertice else edge.v2
            if v not in visited and edge.weight < costs[v]:
                costs[v] = edge.weight
                edges[v] = edge

    return mst
