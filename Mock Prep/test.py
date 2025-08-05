import random
import copy

N = 9
BOX = 3


def count_conflicts(board):
    conflicts = 0
    for i in range(N):
        conflicts += N - len(set(board[i]))
        col = [board[r][i] for r in range(N)]
        conflicts += N - len(set(col))

    for i in range(0, N, BOX):
        for j in range(0, N, BOX):
            box = [board[x][y] for x in range(i, i + BOX) for y in range(j, j + BOX)]
            conflicts += N - len(set(box))
    return conflicts


def get_empty_positions(puzzle):
    return [(i, j) for i in range(N) for j in range(N) if puzzle[i][j] == 0]


def random_fill(puzzle, empty_positions):
    filled = copy.deepcopy(puzzle)
    for i in range(N):
        row_vals = set(filled[i][j] for j in range(N) if filled[i][j] != 0)
        missing_vals = list(set(range(1, 10)) - row_vals)
        random.shuffle(missing_vals)
        index = 0
        for j in range(N):
            if filled[i][j] == 0:
                filled[i][j] = missing_vals[index]
                index += 1
    return filled


def hill_climbing(puzzle):
    empty_positions = get_empty_positions(puzzle)
    current = random_fill(puzzle, empty_positions)
    current_h = count_conflicts(current)

    steps = 0
    max_steps = 10000

    while steps < max_steps:
        neighbor = copy.deepcopy(current)
        row = random.randint(0, N - 1)
        empty_cols = [j for j in range(N) if puzzle[row][j] == 0]
        if len(empty_cols) < 2:
            steps += 1
            continue
        a, b = random.sample(empty_cols, 2)
        neighbor[row][a], neighbor[row][b] = neighbor[row][b], neighbor[row][a]

        neighbor_h = count_conflicts(neighbor)
        if neighbor_h < current_h:
            current = neighbor
            current_h = neighbor_h
            if current_h == 0:
                break
        steps += 1

    return current if current_h == 0 else None


def print_board(board):
    for i, row in enumerate(board):
        print(" ".join(str(val) if val != 0 else "." for val in row))
        if i % 3 == 2 and i != 8:
            print("-" * 21)


puzzle = [
    [0, 0, 0, 0, 9, 0, 2, 0, 0],
    [0, 0, 0, 5, 1, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 2, 0, 0, 5],
    [0, 9, 8, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 3, 9, 0],
    [1, 0, 0, 7, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 4, 9, 0, 0, 0],
    [0, 0, 2, 0, 3, 0, 0, 0, 0],
]

print("Initial Puzzle:")
print_board(puzzle)

solution = hill_climbing(puzzle)

if solution:
    print("\nSolved Sudoku:")
    print_board(solution)
else:
    print("\nFailed to find a solution.")
