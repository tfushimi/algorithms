def dijkstra(graph):
    explored = {1}
    shortest_path = {1: 0}
    while set(graph.keys()).difference(explored):
        candidates = []
        for v in explored:
            for w in graph[v]:
                if w.head not in explored:
                    candidates.append((w.head, shortest_path[v] + w.weight))
        w_star, score = sorted(candidates, key = lambda x: x[1])[0]
        shortest_path[w_star] = score
        explored.add(w_star)
    return shortest_path

if __name__ == '__main__':
    from collections import namedtuple

    Vertex = namedtuple('Vertex', ('head', 'weight'))

    graph = {}
    with open("/Algo2/data/dijkstra.txt") as file:
        for line in file:
            tail, *rest = line.rstrip('\n').rstrip('\t').split('\t')
            vertices = []
            for foo in rest:
                head, weight = foo.split(',')
                vertices.append(Vertex(int(head), int(weight)))
            graph[int(tail)] = vertices

    shortest_path = dijkstra(graph)
    target = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    # target = [x for x in range(1, 9)]
    print([shortest_path[x] for x in target])

