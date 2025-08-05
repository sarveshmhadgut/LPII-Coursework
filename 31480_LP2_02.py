import math
import heapq


class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float("inf")
        self.g = float("inf")
        self.h = 0


ROW = 10
COL = 10


def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


def is_unblocked(grid, row, col):
    return grid[row][col] == 1


def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]


def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5


def trace_path(grid, cell_details, dest):
    path, path_grid = [], []
    row = dest[0]
    col = dest[1]

    for grid_row in grid:
        r = []
        for grid_cell in grid_row:
            r.append(grid_cell)
        path_grid.append(r)

    while not (
        cell_details[row][col].parent_i == row
        and cell_details[row][col].parent_j == col
    ):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    path.append((row, col))
    path.reverse()

    for i in range(len(path)):
        if len(path) == 1:
            path_grid[path[i][0]][path[i][1]] = "O"

        elif i == 0:
            path_grid[path[i][0]][path[i][1]] = "S"

        elif i == len(path) - 1:
            path_grid[path[i][0]][path[i][1]] = "D"

        elif path[i + 1][0] == path[i][0]:
            path_grid[path[i][0]][path[i][1]] = "-"

        elif path[i + 1][1] == path[i][1]:
            path_grid[path[i][0]][path[i][1]] = "|"

        elif (
            path[i + 1][0] > path[i][0]
            and path[i + 1][1] > path[i][1]
            or path[i + 1][0] < path[i][0]
            and path[i + 1][1] < path[i][1]
        ):
            path_grid[path[i][0]][path[i][1]] = "\\"
        else:
            path_grid[path[i][0]][path[i][1]] = "/"

    print(path_grid)
    print()
    print(grid)
    i = 0
    print(
        "\n",
        "Path Grid".rjust(90, " "),
        "\n\t\t\t\t\t\t\t\t_",
        "_".rjust(46, "_"),
        "\n\t\t\t\t\t\t\t\t|",
        "|".rjust(46, " "),
        end="\n\t\t\t\t\t\t\t\t|      ",
    )

    for i in range(len(path_grid)):
        print(i, end="   ")
    print("|\n\t\t\t\t\t\t\t\t|", "|".rjust(46, " "))

    i = 0
    for row in path_grid:
        print("\t\t\t\t\t\t\t\t|", end=f"  {i}:  ")

        for cell in row:
            print(cell, end="   ")
        print("|\n", "\t\t\t\t\t\t\t\t|", "|".rjust(46, " "))
        i += 1

    print("\t\t\t\t\t\t\t\t|", "|".rjust(46, "_"))
    print()
    print("\tPath :", end=" ")
    for i in range(len(path)):
        if i == 0:
            print(f"[S] {path[i]}", end=" -> ")
        elif i == len(path) - 1:
            print(f"{path[i]} [D]")
        else:
            print(path[i], end=" -> ")


def print_heap(open_list):
    for a, b, c in open_list:
        print(f"{a} ({b}, {c})", end=" <- ")
    print("END\n")


def a_star_search(grid, src, dest):
    operations = 0
    max_open_list_size = 0

    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("\n\t\t\t\t\t\t\t\t\tSource or destination is invalid")
        return

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(
        grid, dest[0], dest[1]
    ):
        print("\n\t\t\t\t\t\t\t\t\tSource or the destination is blocked")
        return

    if is_destination(src[0], src[1], dest):
        print("\n\t\t\t\t\t\t\t\t\tWe are already at the destination")
        return

    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    i, j = src
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    open_list = []
    heapq.heappush(open_list, (0.0, i, j))
    max_open_list_size = max(max_open_list_size, len(open_list))

    found_dest = False

    while len(open_list) > 0:
        operations += 1
        p = heapq.heappop(open_list)
        i, j = p[1], p[2]
        closed_list[i][j] = True

        print(
            f"\nProcessing cell ({i}, {j}):-  f: {cell_details[i][j].f:.2f},  g: {cell_details[i][j].g:.2f},  h: {cell_details[i][j].h:.2f}"
        )

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]

            if (
                is_valid(new_i, new_j)
                and is_unblocked(grid, new_i, new_j)
                and not closed_list[new_i][new_j]
            ):
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("\n\t\t\t\t\t\t\t\t\tDestinaton cell reached!")
                    trace_path(grid, cell_details, dest)
                    found_dest = True
                    print(
                        f"\n\tComplexities:\n\t\t Time Complexity: O({operations})\n\t\tSpace Complexity: O({max_open_list_size})"
                    )
                    return
                else:
                    g_new = round(cell_details[i][j].g + 1.0, 2)
                    h_new = round(calculate_h_value(new_i, new_j, dest), 2)
                    f_new = round(g_new + h_new, 2)

                    if (
                        cell_details[new_i][new_j].f == float("inf")
                        or cell_details[new_i][new_j].f > f_new
                    ):
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        max_open_list_size = max(max_open_list_size, len(open_list))
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        print(
                            f"\t({new_i}, {new_j}) cell added to the open list: f = {f_new}, g = {g_new}, h = {h_new}"
                        )
        print("\nUpdated open list: ", end=" ")
        print_heap(open_list)

    if not found_dest:
        print("Failed to find the destination cell")


def main():
    with open("./input2.txt", "r") as f:
        grid = []

        for line in f:
            tokens = line.strip("\n").split(" ")
            grid.append([int(token) for token in tokens])

    flag = 1
    while flag:
        i = 0
        print(
            "\n",
            "Grid".rjust(90, " "),
            "\n\t\t\t\t\t\t\t\t_",
            "_".rjust(46, "_"),
            "\n\t\t\t\t\t\t\t\t|",
            "|".rjust(46, " "),
            end="\n\t\t\t\t\t\t\t\t|      ",
        )
        for i in range(len(grid)):
            print(i, end="   ")
        print("|\n\t\t\t\t\t\t\t\t|", "|".rjust(46, " "))
        i = 0
        for row in grid:
            print("\t\t\t\t\t\t\t\t|", end=f"  {i}:  ")
            for cell in row:
                print(cell, end="   ")
            print("|\n", "\t\t\t\t\t\t\t\t|", "|".rjust(46, " "))
            i += 1
        print("\t\t\t\t\t\t\t\t|", "|".rjust(46, "_"))
        src_i, src_j = input("\n\t     Enter source: (i, j): ").split(" ")
        dest_i, dest_j = input("\tEnter destination: (i, j): ").split(" ")

        src = [int(src_i), int(src_j)]
        dest = [int(dest_i), int(dest_j)]
        a_star_search(grid, src, dest)

        flag = int(input("\n\t\t\t\t\t\t\t\t\tDo you want to quit? '0' if YES: "))
        if not flag:
            print("\n\t\t\t\t\t\t\t\t\tExit operation executed successfully!")


if __name__ == "__main__":
    main()

"""
grid = [
            #0  1  2  3  4  5  6  7  8  9
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1], #0
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1], #1
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 1], #2
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1], #3
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0], #4
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 0], #5
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], #6
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1], #7
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1], #8
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]  #9

        ]
"""
