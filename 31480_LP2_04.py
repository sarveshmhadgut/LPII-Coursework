import shutil


def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur, solutions):
    n = len(cols)

    if i == n:
        solutions.append(cur[:])
        return

    for j in range(n):
        if cols[j] or rightDiagonal[i + j] or leftDiagonal[i - j + n - 1]:
            continue

        cols[j] = 1
        rightDiagonal[i + j] = 1
        leftDiagonal[i - j + n - 1] = 1
        cur.append(j + 1)

        placeQueens(i + 1, cols, leftDiagonal, rightDiagonal, cur, solutions)

        cur.pop()
        cols[j] = 0
        rightDiagonal[i + j] = 0
        leftDiagonal[i - j + n - 1] = 0


def printChessboard(n, solution):
    terminal_width = shutil.get_terminal_size().columns

    board = [["." for _ in range(n)] for _ in range(n)]

    for row in range(n):
        board[row][solution[row] - 1] = "Q"

    empty_row = "|" + " " * (3 * n + 4) + "|"
    board_str = ["_" + "_" * (3 * n + 4) + "_"]

    for row in board:
        row_str = "| " + "   ".join(row) + "  |"

        board_str.append(row_str)
        if row != board[-1]:
            board_str.append(empty_row)
    board_str.append("|" + "_" * (3 * n + 4) + "|")

    with open("output4.txt", "a") as f:
        for line in board_str:
            print(line.center(terminal_width))
            f.write(line + "\n")


def nQueen(n):
    cols = [0] * n
    leftDiagonal = [0] * (n * 2)
    rightDiagonal = [0] * (n * 2)
    cur = []
    solutions = []

    placeQueens(0, cols, leftDiagonal, rightDiagonal, cur, solutions)
    return solutions


def menu():
    terminal_width = shutil.get_terminal_size().columns

    operations = {
        "S": "Set Board Size",
        "V": "View All Solutions",
        "E": "Exit",
    }

    n = None

    while True:
        print()
        print("+--------+-------------+-------------+".center(terminal_width))
        print("| Option |        Description        |".center(terminal_width))
        print("+--------+-------------+-------------+".center(terminal_width))
        for key, value in operations.items():
            print(f"| {key.upper():^6} | {value:^25} |".center(terminal_width))
        print("+--------+-------------+-------------+".center(terminal_width))

        print("Enter your option -> ".center(terminal_width), end="")
        choice = input().strip().upper()

        if choice == "E":
            print("Exit Operation Exexuted Successfully!".center(terminal_width))
            break

        elif choice == "S":
            try:
                print(
                    "Enter the value of board size -> ".center(terminal_width), end=""
                )
                n = int(input().strip())

                if n < 1:
                    raise ValueError
                print(f"Chess board size is set to {n}.".center(terminal_width))
            except ValueError:
                print(
                    "Invalid input! Please enter a positive integer.".center(
                        terminal_width
                    )
                )

        elif choice == "V":
            if n is None:
                print(
                    "Please set a board size first (Option 'S').".center(terminal_width)
                )
                continue

            solutions = nQueen(n)

            if not solutions:
                print("No solution exists.".center(terminal_width))
            else:
                print(f"Chess board size is {n}.".center(terminal_width))
                with open("output4.txt", "w") as f:
                    f.truncate(0)
                    f.write(f"Chess board size: {n}.")

                for idx, solution in enumerate(solutions, 1):
                    print()
                    print(f"Solution {idx}:".center(terminal_width))

                    with open("output4.txt", "a") as f:
                        f.write("\n")
                        f.write(f"Solution {idx}:" + "\n")

                    printChessboard(n, solution)
        else:
            print("Invalid choice! Please try again.".center(terminal_width))

        print()
        print("\n", "Press Enter to continue...".center(terminal_width), end="")
        input()


if __name__ == "__main__":
    menu()
