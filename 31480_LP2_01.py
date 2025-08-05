from collections import deque
import time


class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
            if node1 in self.graph[node2]:
                self.graph[node2].remove(node1)

    def remove_node(self, node):
        if node in self.graph:
            for neighbor in self.graph[node]:
                self.graph[neighbor].remove(node)
            del self.graph[node]

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"\t{node} -> {' '.join(neighbors)}")

    def get_neighbors(self, node):
        return self.graph.get(node, [])


def dfs_recursive(graph, start, visited=None, searchKey="#", searchIdx=0):
    if visited is None:
        visited = set()

    visited.add(start)
    searchIdx += 1

    if searchKey == "#":
        print(start, end=" -> ")
    elif start == searchKey:
        print(f"\tDFS index for {searchKey.upper()}: {searchIdx}")
        return

    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, searchKey, searchIdx)


def bfs_recursive(graph, queue, visited=None, searchKey="#", searchIdx=0):
    if visited is None:
        visited = set()

    if not queue:
        return

    node = queue.popleft()
    if node not in visited:
        searchIdx += 1
        if searchKey == "#":
            print(node, end=" -> ")
        elif node == searchKey:
            print(f"\tBFS index for {searchKey.upper()}: {searchIdx}")
            return

        visited.add(node)
        queue.extend(graph.get_neighbors(node))

    bfs_recursive(graph, queue, visited, searchKey, searchIdx)


def main(graph, startNode):
    print(f"\nGraph Representation:")
    g.display()

    print(f"\nTraversals starting with node: {startNode}")
    print("\n\tDFS (Recursive)", end=" : ")
    dfs_recursive(graph, startNode)
    print("END")

    print("\n\tBFS (Recursive)", end=" : ")
    bfs_recursive(graph, deque([startNode]))
    print("END")

    searchKey = input("\nEnter search key -> ").upper()
    print(f"Searching for Node '{searchKey}' using DFS and BFS:\n")
    dfs_recursive(graph, startNode, searchKey=searchKey)
    print()
    bfs_recursive(graph, deque([startNode]), searchKey=searchKey)
    print(
        "  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
    )


if __name__ == "__main__":
    # * Example 1
    """
         A -- B
         \  /
          C -- F
         /    /
        D -- E

    G -- H
     \  /
      I"""

    g = UndirectedGraph()
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

    main(g, "A")
    time.sleep(5)

    # * Example 2
    """
               1
             /  \
            2    3
           / \  / \
          4   5 6  7
         /    \
        8      9
                \
                10
    """
    g = UndirectedGraph()
    g.add_edge("1", "2")
    g.add_edge("1", "3")
    g.add_edge("2", "4")
    g.add_edge("2", "5")
    g.add_edge("3", "6")
    g.add_edge("3", "7")
    g.add_edge("4", "8")
    g.add_edge("5", "9")
    g.add_edge("6", "10")

    main(g, "1")
    time.sleep(5)

    # * Example 3
    """
         A
        / \
        B  C
      / |   \
     D  E    F
        \   /
        G--H
    """
    g = UndirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("E", "G")
    g.add_edge("C", "F")
    g.add_edge("F", "H")
    g.add_edge("G", "H")

    main(g, "A")
