def first_dfs(graph, node, current_finishing_time, finishing_times, explored):
    stack = [node]
    while stack:
        vertex = stack[-1]
        explored.add(vertex)
        is_added = False
        for neighbor in graph.get(vertex, []):
            if neighbor not in explored:
                is_added = True
                stack.append(neighbor)
        if not is_added :
            top = stack.pop()
            # a node can be in stack multiple times if it has multiple in-coming edges
            if top not in finishing_times:
                current_finishing_time += 1
                finishing_times[top] = current_finishing_time
    return current_finishing_time

def second_dfs(graph, node, explored):
    stack = [node]
    scc = set()
    while stack:
        vertex = stack.pop()
        explored.add(vertex)
        scc.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in explored:
                stack.append(neighbor)
    return scc

if __name__ == '__main__':
    from collections import defaultdict

    graph, graph_rev = defaultdict(list), defaultdict(list)
    N = -1
    with open("/Users/Takahiro/MyProjects/Algorithms/Algo2/data/scc.txt") as file:
        for line in file:
            tail, head = [int(x) for x in line.split()]
            N = max(N, max(tail, head))
            # original graph
            graph[tail].append(head)
            # reversed graph
            graph_rev[head].append(tail)

    finishing_times, explored = dict(), set()
    current_finishing_time = 0
    for i in reversed(range(1, N+1)):
        if i not in explored:
            current_finishing_time = first_dfs(graph_rev, i, current_finishing_time, finishing_times, explored)

    sccs, explored = dict(), set()
    for i in [key for key, _ in sorted(finishing_times.items(), key = lambda item: item[1], reverse=True)]:
        if i not in explored:
            new_scc = second_dfs(graph, i, explored)
            sccs[i] = new_scc

    print(sorted([len(sccs[key]) for key in sccs.keys()], reverse=True)[:5])