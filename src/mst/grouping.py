
from adt import UnionFind


def split_in_groups(edges, n=2):
    vertices = list({edge.v1 for edge in edges} | {edge.v2 for edge in edges})

    components = UnionFind(len(vertices))

    edges = sorted(edges, key=lambda x: x.weight)[:-1 * (n-1)]

    for edge in edges:
        v1_index = vertices.index(edge.v1)
        v2_index = vertices.index(edge.v2)
        components.union(v1_index, v2_index)

    groups = {}
    for i, vertice in enumerate(vertices):
        group_id = components.find(i)
        if group_id not in groups:
            groups[group_id] = []

        groups[group_id].append(vertice)

    return groups.values()
