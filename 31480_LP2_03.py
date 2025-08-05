import os
import heapq
import shutil
import math

terminal_width = shutil.get_terminal_size().columns


def clear_terminal():
    os_name = os.name
    if os_name == "nt":
        os.system("cls")
    elif os_name == "posix":
        os.system("clear")


class Graph:
    def __init__(self):
        self.edges = []
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        self.edges.append((weight, u, v))
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if ":" not in line:
                    continue
                node_part, connections_part = line.split(":", 1)
                node = node_part.strip()

                for connection in connections_part.split():
                    connection = connection.strip()
                    if "(" in connection and ")" in connection:
                        neighbor, weight = connection.split("(")
                        neighbor = neighbor.strip()
                        weight = int(weight.split(")")[0])
                        self.add_edge(node, neighbor, weight)

    def display_graph(self):
        clear_terminal()
        print("\n\n", "Graph Representation".center(terminal_width))
        print(
            "+------+-------------+-------------+-------------+-------------+-------------+".center(
                terminal_width
            )
        )
        print(
            "| Node |                         Connected Vertices                          |".center(
                terminal_width
            )
        )
        print(
            "+------+-------------+-------------+-------------+-------------+-------------+".center(
                terminal_width
            )
        )
        for node in sorted(self.adj_list.keys()):
            connections = ", ".join(
                [f"{v} [{str(w).zfill(2)}]" for v, w in self.adj_list[node]]
            )
            print(f"| {node:^4} | {connections:<67} |".center(terminal_width))
            # print(f"| {".":^4} | {".":<39} |".center(terminal_width))
        print(
            "+------+-------------+-------------+-------------+-------------+-------------+".center(
                terminal_width
            )
        )


def dijkstra(graph: Graph, src):
    pq = []
    nodes_visited = 0
    edges_examined = 0
    heapq.heappush(pq, (0, src))

    dist = {node: float("inf") for node in graph.adj_list}
    prev = {node: None for node in graph.adj_list}
    dist[src] = 0

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph.adj_list[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    return dist, prev


def prim(graph: Graph, start=None):
    mst = []
    visited = set()
    nodes_visited = 0
    edges_examined = 0

    if start is None:
        start = min(graph.adj_list.keys())

    pq = [(0, start, None)]

    while pq and len(visited) < len(graph.adj_list):
        weight, u, parent = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)
        nodes_visited += 1
        if parent is not None:
            mst.append((parent, u, weight))

        for v, w in graph.adj_list[u]:
            edges_examined += 1
            if v not in visited:
                heapq.heappush(pq, (w, v, u))

    if len(visited) < len(graph.adj_list):
        print("Warning: Graph is disconnected. MST may be incomplete.")

    return mst, nodes_visited, edges_examined


def kruskal(graph: Graph):
    parent = {}
    rank = {}
    edges_examined = 0
    nodes_connected = 0

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    for node in graph.adj_list:
        parent[node] = node
        rank[node] = 0

    mst = []
    graph.edges.sort()

    for weight, u, v in graph.edges:
        edges_examined += 1
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            nodes_connected += 1

        if len(mst) == len(graph.adj_list) - 1:
            break

    if len(mst) != len(graph.adj_list) - 1:
        print("Warning: Graph is disconnected. MST may be incomplete.")

    return mst, nodes_connected, edges_examined


def display_shortest_paths(dist, prev):
    print("\n\n", "Shortest Paths using Djikstras'".center(terminal_width))
    print("+------+----------+-------------+".center(terminal_width))
    print("| Node | Distance | Predecessor |".center(terminal_width))
    print("+------+----------+-------------+".center(terminal_width))
    for node in sorted(dist.keys()):
        pred = prev[node] if prev[node] is not None else "None"
        print(f"| {node:^4} | {dist[node]:^8} | {pred:^11} |".center(terminal_width))
        # print(f"| {"":^4} | {"":^8} | {"":^11} |".center(terminal_width))
    print("+------+----------+-------------+".center(terminal_width))


def display_mst(mst, nodes_visited, edges_examined, algo):
    total_cost = sum(weight for _, _, weight in mst)

    print("\n\n", f"Minimum Spanning Tree using {algo}".center(terminal_width))
    print("+-------+-------+--------+".center(terminal_width))
    print("| Node1 | Node2 | Weight |".center(terminal_width))
    print("+-------+-------+--------+".center(terminal_width))

    for u, v, weight in mst:
        print(f"| {u:^5} | {v:^5} | {weight:^6} |".center(terminal_width))
        # print(f"| {"":^5} | {"":^5} | {"":^6} |".center(terminal_width))

    print("+-------+-------+--------+".center(terminal_width))
    print(f"Total Minimum Cost: {total_cost}".center(terminal_width))

    print()
    print(f"Nodes visited -> {nodes_visited}".center(terminal_width))
    print(f"Edges visited -> {edges_examined}".center(terminal_width))
    print()
    print(
        f"Estimated Time Complexity O(E log V) -> O({edges_examined} log({nodes_visited})) ->  {edges_examined * math.log(nodes_visited)}".center(
            terminal_width
        )
    )

    print(
        f"Space Complexity O(V + E) -> O({nodes_visited} + {edges_examined}) -> {nodes_visited + edges_examined}".center(
            terminal_width
        )
    )


def main():
    clear_terminal()
    operations = {
        "C": "Change Input File",
        "P": "Print Graph",
        "R": "Prim's Algorithm",
        "K": "Kruskal's Algorithm",
        "D": "Dijkstra's Algorithm",
        "E": "Exit",
    }

    g = Graph()
    g.read_from_file("input3.txt")

    while True:
        print()
        print("+--------+-------------+-------------+".center(terminal_width))
        print("| Option |        Description        |".center(terminal_width))
        print("+--------+-------------+-------------+".center(terminal_width))
        for key, value in operations.items():
            print(f"| {key.upper():<6} | {value:<25} |".center(terminal_width))
            # print(f"| {"":<6} | {"":<25} |".center(terminal_width))
        print("+--------+-------------+-------------+".center(terminal_width))

        print("Enter your option -> ".center(terminal_width), end="")
        choice = input().strip().upper()

        if choice.upper() == "E":
            print("Exit Operation Executed Successfully!".center(terminal_width))
            break

        elif choice.upper() == "C":
            print("Enter your file name -> ".center(terminal_width), end="")
            file_name = input().strip()
            g.read_from_file(file_name)

        elif choice.upper() == "P":
            g.display_graph()

        elif choice == "D":
            print("Enter starting node-> ".center(terminal_width), end="")
            start_node = input().strip().upper()
            dist, prev = dijkstra(g, start_node)
            display_shortest_paths(dist, prev)

        elif choice.upper() == "K":
            mst, nodes, edges = kruskal(g)
            display_mst(mst, nodes, edges, "Kruskal's")

        elif choice.upper() == "R":
            print("Enter starting node-> ".center(terminal_width), end="")
            start_node = input().strip().upper()
            mst, nodes, edges = prim(g, start_node)
            display_mst(mst, nodes, edges, "Prim's")

        else:
            print("Invalid choice! Please try again.".center(terminal_width))

        print()
        print("Press Enter to continue...".center(terminal_width), end="")
        input()


if __name__ == "__main__":
    main()

# g = Graph()
# g.read_from_file("input3.txt")

# g.display_graph()

# dists, paths = dijkstra(g, "C")
# display_shortest_paths(dists, paths)

# mst_prim = prim(g, "A")
# display_mst(mst_prim, "Prims'")

# mst_kruskal = kruskal(g)
# display_mst(mst_kruskal, "Kruskals'")
