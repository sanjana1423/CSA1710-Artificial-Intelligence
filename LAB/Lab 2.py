
def solve(board, row):
    if row == 8:
        for i in range(8):
            print(board[i])
        return True

    for col in range(8):
        safe = True

        for i in range(row):
            if (board[i] == col or
                abs(board[i] - col) == abs(i - row)):
                safe = False
                break

        if safe:
            board[row] = col

            if solve(board, row + 1):
                return True

    return False

board = [-1] * 8

if solve(board, 0):
    print("Solution found")
else:
    print("No solution")
