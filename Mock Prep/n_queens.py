def n_queens(n):
    solutions = []
    board = [-1] * n

    def backtrack(row, cols, diagonal1, diagonal2):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if col in cols or row + col in diagonal1 or row - col in diagonal2:
                continue

            board[row] = col
            cols.add(col)
            diagonal1.add(row + col)
            diagonal2.add(row - col)

            backtrack(row + 1, cols, diagonal1, diagonal2)

            cols.remove(col)
            diagonal1.remove(row + col)
            diagonal2.remove(row - col)

    backtrack(0, set(), set(), set())
    return solutions


a = n_queens(4)
print(a)
