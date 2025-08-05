import heapq


class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def a_star(grid, start, goal):

    if grid[start[0]][start[1]] == 1:
        print("Start state is blocked!")
        return None

    if grid[goal[0]][goal[1]] == 1:
        print("Goal state is blocked!")

    open_list = []
    heapq.heappush(open_list, Node(start, None, 0, heuristic(start, goal)))
    close_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        current_position = current_node.position

        if current_position == goal:
            path = []
            while current_node:
                path.insert(0, current_node.position)
                current_node = current_node.parent

            return path

        close_list.add(current_position)
        x, y = current_position
        for dx, dy in [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]:
            neighbor = (x + dx, y + dy)
            if (
                0 <= neighbor[0] < len(grid)
                and 0 <= neighbor[1] < len(grid[0])
                and grid[neighbor[0]][neighbor[1]] != "."
                and neighbor not in close_list
            ):

                move_cost = 1.41 if dx != 0 and dy != 0 else 1
                g_cost = current_node.g + move_cost
                h_cost = heuristic(neighbor, goal)
                neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

                skip = False
                for n in open_list:
                    if n.position == neighbor and n.f <= neighbor_node.f:
                        skip = True
                        break

                if not skip:
                    heapq.heappush(open_list, neighbor_node)

    return None


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
]

grid = []
with open("./input2.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip().split(" ")))

print("_" * (3 + len(grid[0]) * 2))
grid = [[" " if cell == "0" else "." for cell in row] for row in grid]
for row in grid:
    print("|", " ".join(map(str, row)), "|")
print("|", "_" * (len(grid[0]) * 2 - 1), "|")

start = (0, 0)
goal = (9, 3)

path = a_star(grid, start, goal)
if path:
    print(f"\nPath length: {len(path) - 1}\n")
else:
    print("\nNo path found!\n")

# print("2190\u2190", ..... \u2199)
directions = {
    (-1, 0): "\u2191",
    (1, 0): "\u2193",
    (0, -1): "\u2190",
    (0, 1): "\u2192",
    (-1, -1): "\u2196",
    (-1, 1): "\u2197",
    (1, -1): "\u2199",
    (1, 1): "\u2198",
}

for i in range(len(path)):
    x, y = path[i]
    if path[i] == goal:
        grid[path[i][0]][path[i][1]] = "G"

    elif path[i] == start:
        grid[path[i][0]][path[i][1]] = "S"

    elif i + 1 < len(path):
        dx, dy = path[i + 1][0] - x, path[i + 1][1] - y
        grid[x][y] = directions[(dx, dy)]

print("_" * (3 + len(grid[0]) * 2))
for row in grid:
    print("|", " ".join(map(str, row)), "|")
print("|", "_" * (len(grid[0]) * 2 - 1), "|")
