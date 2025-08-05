import heapq
import time
import os


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


class Graph:
    def __init__(self):
        self.edges = []
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        self.adj_list.setdefault(u, []).append((v, weight))
        self.adj_list.setdefault(v, []).append((u, weight))
        self.edges.append((weight, u, v))

    def read_from_file(self, filename):
        self.edges.clear()
        self.adj_list.clear()

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
                    if "'" not in connection:
                        continue
                    neighbor, weight = connection.split("'")
                    neighbor = neighbor.strip()
                    weight = int(weight.strip())
                    self.add_edge(node, neighbor, weight)

    def display_graph(self):
        print("\nGraph:")
        for node in sorted(self.adj_list):
            connections = ", ".join(f"{v} [{w}]" for v, w in self.adj_list[node])
            print(f"{node}: {connections}")


def dijkstra(graph, src):
    pq = [(0, src)]
    dist = {node: float("inf") for node in graph.adj_list}
    prev = {node: None for node in graph.adj_list}
    dist[src] = 0

    while pq:
        current_dist, u = heapq.heappop(pq)
        for v, weight in graph.adj_list[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))
    return dist, prev


def prim(graph, start):
    mst, visited = [], set()
    pq = [(0, start, None)]

    while pq:
        weight, u, parent = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if parent is not None:
            mst.append((parent, u, weight))
        for v, w in graph.adj_list[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v, u))
    return mst


def display_shortest_paths(dist, prev):
    print("\nDijkstra's Shortest Paths:")
    print("\nNode  Distance  Predecessor\n")

    for node in sorted(dist):
        predecessor = prev[node] if prev[node] is not None else "None"
        print(f"{node:^4}{dist[node]:^12}{predecessor:^12}")


def display_mst(mst, algo):
    total_cost = sum(w for _, _, w in mst)
    print(f"\nPrim's MST:")
    print("\nNode1  Node2  Weight\n")
    for u, v, w in mst:
        print(f"{u:^6} {v:^6} {w:^6}")
    print(f"Total Cost: {total_cost}")


def main():
    g = Graph()
    g.read_from_file("input3.txt")

    while True:
        print(
            "\nS: Selection Sort\nP: Display Graph\nR: Prim's MST\nD: Dijkstra's Shortest Path\nE: Exit"
        )
        choice = input("Enter choice: ").strip().upper()

        if choice == "E":
            break
        elif choice == "S":
            arr_vals = input("Enter array elements: ")
            arr = [int(elem) for elem in arr_vals.split(" ")]
            print("\nOriginal Array: ", arr)
            sorted_array = selection_sort(arr)
            print("Sorted Array: ", sorted_array)

        elif choice == "P":
            g.display_graph()
        elif choice == "D":
            start = input("Start node: ").strip().upper()
            dist, prev = dijkstra(g, start)
            display_shortest_paths(dist, prev)
        elif choice == "R":
            start = input("Start node: ").strip().upper()
            mst = prim(g, start)
            display_mst(mst, "Prim's")
        else:
            print("Invalid choice!")

        time.sleep(5)


if __name__ == "__main__":
    main()
