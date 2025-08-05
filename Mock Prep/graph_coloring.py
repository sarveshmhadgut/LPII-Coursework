def is_safe_matrix(graph, color, node, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True


def get_unassigned_node(graph, color, m):
    unassigned = [v for v in range(len(graph)) if color[v] == 0]
    if not unassigned:
        return None

    def count_legal_colors(v):
        return sum(is_safe_matrix(graph, color, v, c) for c in range(1, m + 1))

    return min(unassigned, key=count_legal_colors)


def backtrack(graph, m, color):
    if all(c != 0 for c in color):
        return True

    node = get_unassigned_node(graph, color, m)
    if node is None:
        return False

    for c in range(1, m + 1):
        if is_safe_matrix(graph, color, node, c):
            color[node] = c
            if backtrack(graph, m, color):
                return True
            color[node] = 0
    return False


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n
    if not backtrack(graph, m, color):
        print("No solution exists with", m, "colors.")
    else:
        print("Solution:", {i: color[i] for i in range(n)})


adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
]

k = 3
graph_coloring(adj_matrix, k)
