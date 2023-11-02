#!/usr/bin/python3
"""Solves the N queens puzzle"""


import sys


def solve_nqueens(row, col):
    solution = [[]]
    for queen in range(row):
        solution = solve(queen, col, solution)
    return solution


def solve(queen, col, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(col):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(board, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[col] - x) != board - col
                   for col in range(board))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    solutions = solve_nqueens(n, n)
    for array in solutions:
        clean = []
        for board, x in enumerate(array):
            clean.append([board, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
