#!/usr/bin/python3
""" A script that solve the nqueens problem """

import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at position (row, col) is safe."""
    # Check the row and column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """Solve the N-Queens problem using backtracking."""
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nqueens(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False


def print_solution(board):
    """Print the chessboard with the queens placed."""
    for row in board:
        print(" ".join(str(i) for i in row))


def nqueens(n):
    """Initialize the board and start solving the N-Queens problem."""
    board = [[0] * n for _ in range(n)]
    if solve_nqueens(board, 0, n):
        print_solution(board)
    else:
        print("No solution exists")


# Example Usage
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(sys.argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)
else:
    nqueens(sys.argv[1])
