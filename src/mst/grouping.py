
from adt import UnionFind


# def get_vertice_groups(edges):
#     groups = {}
#     for i, vertice in enumerate(vertices):
#         group_id = components.find(i)
#         if group_id not in groups:
#             groups[group_id] = []
#
#         groups[group_id].append(vertice)
#
#     return list(groups.values())


def split_in_groups(edges, n=2):
    vertices = list({edge.v1 for edge in edges} | {edge.v2 for edge in edges})

    components = UnionFind()
    for vertice in vertices:
        components.add_vertice(vertice.x, vertice.y)

    edges = sorted(edges, key=lambda x: x.weight)[:-1 * (n-1)]

    for edge in edges:
        components.union(edge.v1, edge.v2)

    return components.groups()
