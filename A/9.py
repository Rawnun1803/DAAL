def is_safe(board, row, col):
    for i in range(row):
        # Check same column and diagonal
        if board[i] == col or abs(board[i] - col) == row - i:
            return False

    return True


def solve_nqueens(board, row, n):
    global steps
    steps += 1

    # All queens placed successfully
    if row == n:
        print("\nSolution found!")

        for col in board:
            print(" ".join("Q" if j == col else "." for j in range(n)))

        return True

    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            print(f"Step {steps}: Place Q at row {row}, col {col}")

            if solve_nqueens(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1
            print(f"Step {steps}: Backtrack from row {row}, col {col}")

    return False


# Main program
n = int(input("Enter number of queens (N): "))

if n < 1:
    print("N must be at least 1.")

else:
    board = [-1] * n
    steps = 0

    if not solve_nqueens(board, 0, n):
        print(f"No solution exists for N = {n}")