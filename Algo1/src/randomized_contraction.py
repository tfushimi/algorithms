"""
Divide and Conquer, Sorting and Searching, and Randomized Algorithms
Programming assignment4
"""
import random

def random_contraction(edge_dict):
    """
    Finds a minimum cut using Randomized Contraction Algorithm.
    The returned value is not always the minimum cut due to the nature of the algorithm.
    To get the minimum cut, this function needs to be called multiple times.

    Args:
    edge_list:  a list of edges in the graph

    Returns:
    a minimum cut
    """
    while len(edge_dict) > 2:
        # randomly choose an edge
        left = random.choice(list(edge_dict.keys()))
        right = random.choice(edge_dict[left])
        # remove left vertex from the neighbor set of the right vertex
        edge_dict[right] = [x for x in edge_dict[right] if x != left]
        # remove right vertex from the neighbor set of the left vertex
        edge_dict[left] = [x for x in edge_dict[left] if x != right]
        # contraction: (left, right) => left
        # concatenate the neighbor set of the right vertex to that of the left vertex
        edge_dict[left] += edge_dict[right]
        # replace the right vertex by the left vertex in the neighbor set of other vertices
        history = set()
        for vertex in edge_dict[right]:
            if vertex not in history:
                history.add(vertex)
                edge_dict[vertex] = [x if x != right else left for x in edge_dict[vertex]]
        # remove the right vertex from edge list
        edge_dict.pop(right)
    # get one of the two edges
    a_key = list(edge_dict.keys())[0]
    return len(edge_dict[a_key])

if __name__ == '__main__':
    from copy import deepcopy
    from collections import defaultdict

    # Read data
    original_edge_dict = dict()  # original edge list
    with open("AdjacencyList.txt") as file:
        for line in file:
            token = line.split()
            original_edge_dict[token[0]] = token[1:]

    # Run Randomized Contraction algorithm 100 times
    min_cut_dict = defaultdict(int)
    for trial in range(100):
        # make a deep copy because random_contraction modifies a list in place
        edge_dict = deepcopy(original_edge_dict)
        # find a minimum cut
        min_cut = random_contraction(edge_dict)
        min_cut_dict[min_cut] += 1
        print("Trial: %d, Min cut: %d" % (trial+1, min_cut))
    print("Min cut is %d" % min(min_cut_dict.keys()))