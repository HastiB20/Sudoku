#!/usr/bin/env python
# coding: utf-8

# In[4]:


def solve_sudoku(board):
    if not find_empty_cell(board):
        return True

    row, col = find_empty_cell(board)
    available_numbers = get_available_numbers(board, row, col)

    for num in available_numbers:
        board[row][col] = num

        if solve_sudoku(board):
            return True

        board[row][col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def get_available_numbers(board, row, col):
    available_numbers = set(range(1, 10))

    # Remove numbers in the same row
    for j in range(9):
        if board[row][j] in available_numbers:
            available_numbers.remove(board[row][j])

    # Remove numbers in the same column
    for i in range(9):
        if board[i][col] in available_numbers:
            available_numbers.remove(board[i][col])

    # Remove numbers in the same 3x3 box
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] in available_numbers:
                available_numbers.remove(board[start_row + i][start_col + j])

    return available_numbers


# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists.")


# def solve_sudoku(board):
#     if not find_empty_cell(board):
#         return True
# 
#     row, col = find_empty_cell(board)
#     available_numbers = get_available_numbers(board, row, col)
# 
#     for num in available_numbers:
#         board[row][col] = num
# 
#         if solve_sudoku(board):
#             return True
# 
#         board[row][col] = 0
# 
#     return False
# 
# 
# def find_empty_cell(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return i, j
#     return None
# 
# 
# def get_available_numbers(board, row, col):
#     available_numbers = set(range(1, 10))
# 
#     # Remove numbers in the same row
#     for j in range(9):
#         if board[row][j] in available_numbers:
#             available_numbers.remove(board[row][j])
# 
#     # Remove numbers in the same column
#     for i in range(9):
#         if board[i][col] in available_numbers:
#             available_numbers.remove(board[i][col])
# 
#     # Remove numbers in the same 3x3 box
#     start_row = 3 * (row // 3)
#     start_col = 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if board[start_row + i][start_col + j] in available_numbers:
#                 available_numbers.remove(board[start_row + i][start_col + j])
# 
#     return available_numbers
# 
# 
# # Example Sudoku board
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# 
# if solve_sudoku(board):
#     print("Solution:")
#     for row in board:
#         print(row)
# else:
#     print("No solution exists.")
# 
