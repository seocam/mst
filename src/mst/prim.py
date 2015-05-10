
from adt import MinHeap, Graph, UnionFind

INFINITY = 2 ** 64


def remove_heaviest_edges(graph, n):
    components = UnionFind.from_graph(graph)

    edges = sorted(graph.edges, key=lambda x: x.weight)
    if n:
        edges = edges[:-n]

    for edge in edges:
        components.union(edge.v1, edge.v2)

    return components.groups()


def prim(g, groups=1):
    visited = set()

    edges = {}
    costs = MinHeap()

    for vertice in g.vertices:
        costs[vertice] = INFINITY
        edges[vertice] = None

    mst = Graph()

    for p, vertice in costs:
        visited.add(vertice)

        if edges[vertice] is not None:
            mst.add_edge(edge=edges[vertice])
            edges[vertice].mst = True

        for edge in vertice.edges:
            v = edge.v1 if edge.v1 != vertice else edge.v2
            if v not in visited and edge.weight < costs[v]:
                costs[v] = edge.weight
                edges[v] = edge

    return remove_heaviest_edges(mst, groups-1)
