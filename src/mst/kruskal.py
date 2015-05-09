
from adt import UnionFind


def kruskal(g, groups=1):
    edges = sorted(g.edges, key=lambda x: x.weight)

    group_count = len(g.vertices)
    components = UnionFind.from_graph(g)

    for edge in edges:
        if not components.connected(edge.v1, edge.v2):
            components.union(edge.v1, edge.v2)
            edge.mst = True
            group_count -= 1

        if group_count == groups:
            break

    return components.groups()
