#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""
import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with spaces."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r in range(len(board)) for c in range(len(board[r])) if board[r][c] == "Q"]

def xout(board, row, col):
    """X out spots on a chessboard where non-attacking queens can no longer be placed."""
    n = len(board)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        x, y = row, col
        while 0 <= x + dx < n and 0 <= y + dy < n:
            x += dx
            y += dy
            board[x][y] = "x"

def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = recursive_solve(init_board(n), 0, 0, [])
    for solution in solutions:
        print(solution)