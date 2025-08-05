from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)

            if node1 in self.graph[node2]:
                self.graph[node2].remove(node1)

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} -> {"  ".join(neighbors)}")


def dfs(graph, start, visited=None):
    if visited == None:
        visited = set()

    visited.add(start)

    print(start, end=" -> ")
    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, queue, visited=None):
    if not queue:
        return

    if visited == None:
        visited = set()

    curr = queue.popleft()
    visited.add(curr)
    print(curr, end=" -> ")

    neighbors = graph.get_neighbors(curr)
    for neighbor in neighbors:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    bfs(graph, queue, visited)


def bfs_search(graph, queue, searchKey, visited=None, searchIdx=0):
    if not queue:
        return False, searchIdx, visited
    if visited == None:
        visited = list()

    curr = queue.popleft()
    searchIdx += 1
    visited.append(curr)
    if curr == searchKey:
        return True, searchIdx, visited

    neighbors = graph.get_neighbors(curr)
    for neighbor in neighbors:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    return bfs_search(graph, queue, searchKey, visited, searchIdx)


def dfs_search(graph, start, visited=None, searchKey="#", searchIdx=0):
    if visited == None:
        visited = list()

    visited.append(start)
    searchIdx += 1
    if start == searchKey:
        return True, searchIdx, visited

    neighbors = graph.get_neighbors(start)
    for neighbor in neighbors:
        if neighbor not in visited:
            found, searchIdx, visited = dfs_search(
                graph, neighbor, visited, searchKey, searchIdx
            )
            if found:
                return True, searchIdx, visited

    return False, searchIdx, visited


def main():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")
    g.add_edge("E", "F")
    g.add_edge("F", "C")
    g.add_edge("G", "H")
    g.add_edge("H", "I")
    g.add_edge("I", "G")

    print("\nGraph")
    g.print_graph()

    print("\nDFS Traversal")
    dfs(g, "A")
    print("END")

    print("\nDFS Search")
    a, b, c = dfs_search(graph=g, start="A", searchKey="D")
    if a:
        print("Found at index ", b)
    else:
        print("Not found")

    print("\nBFS Traversal")
    bfs(g, deque(["A"]))
    print("END")

    print("\nBFS Search")
    a, b, c = bfs_search(g, deque(["A"]), searchKey="D")
    if a:
        print("Found at index ", b)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
