
import sys
import itertools

from optparse import OptionParser

from adt import Graph
from mst import kruskal, prim


def parse_input():

    algorithm_choices = ['prim', 'kruskal']

    parser = OptionParser()
    parser.add_option("-a", "--mst-algorithm", dest="algorithm",
                      type='choice', choices=algorithm_choices,
                      help=("MST algorithm to use. Valid choices "
                            "are {}".format(algorithm_choices)))
    parser.add_option("-k", "--number-of-groups", type="int",
                      dest="number_of_groups", default=7,
                      help=("Number of groups to classify the data."
                            " Defaults: 7"))
    parser.add_option("--csv", action='store_true', default=False, dest="csv",
                      help=("Print groups in CSV format."))
    parser.add_option("--rand-index", dest="rand_index",
                      help=("The cluster file to compare results to"))

    (options, args) = parser.parse_args()

    if not options.algorithm:
        parser.error('mst-algorithm must be provided.')

    data = []
    for line in sys.stdin:
        x, y = line.strip().split('\t')
        data.append((float(x), float(y)))

    return (options.algorithm, options.number_of_groups, data,
            options.csv, options.rand_index)


def get_group_coords(groups):
    coords = {}
    for i, group in enumerate(groups):
        coords[i] = {'x': [], 'y': []}

        for vertice in group:
            coords[i]['x'].append('{}'.format(vertice.x))
            coords[i]['y'].append('{}'.format(vertice.y))

    return coords


def print_groups_to_csv(groups):
    coords = get_group_coords(groups)
    for group in coords.values():
        print(';'.join(group['x']) + ';')
        print(';'.join(group['y']) + ';')


def index_groups(groups):
    group_dict = {}
    for i, group in enumerate(groups):
        for vertice in group:
            group_dict[(vertice.x, vertice.y)] = i
    return group_dict


def group(alg, k, data):
    graph = Graph()

    for coordinates in data:
        graph.add_connected_vertice(*coordinates)

    if alg == 'prim':
        mst = prim(graph, k)
    else:
        mst = kruskal(graph, k)

    return mst


def print_groups(data, groups):
    for coordinates in data:
        print(groups[coordinates])


def compare_groups(data, groups, reference_filename):
    reference_groups = {}
    with open(reference_filename) as reference_file:
        for i, line in enumerate(reference_file):
            group = int(line.strip())
            reference_groups[data[i]] = group

    combinations = itertools.combinations(data, 2)

    aggreements = disagreement = 0
    for coords1, coords2 in combinations:
        same_on_ref = reference_groups[coords1] == reference_groups[coords2]
        same_on_result = groups[coords1] == groups[coords2]

        if same_on_ref == same_on_result:
            aggreements += 1
        else:
            disagreement += 1

    print('Rand Index: {}'.format(aggreements/float(aggreements+disagreement)))


def main():
    alg, k, data, csv, rand_index = parse_input()
    groups = group(alg, k, data)
    indexed_groups = index_groups(groups)

    if csv:
        print_groups_to_csv(groups)
    else:
        print_groups(data, indexed_groups)

    if rand_index:
        compare_groups(data, indexed_groups, rand_index)


if __name__ == '__main__':
    main()
