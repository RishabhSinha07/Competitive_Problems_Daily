
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

import copy


def checkN(tempBoard, i, j, count):
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if i+ii >= 0 and i+ii < len(tempBoard) and j+jj >= 0 and j+jj < len(tempBoard[i]):
                if tempBoard[i+ii][j+jj] == 1:
                    count += 1
    return count


def gameOfLife(board):

    tempBoard = copy.deepcopy(board)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                N = checkN(tempBoard, i, j, 0)-1
                if N < 2 or N > 3:
                    board[i][j] = 0
                    continue
                if N >= 2 and N <= 3:
                    board[i][j] = 1
                    continue
            if board[i][j] == 0:
                N = checkN(tempBoard, i, j, 0)
                if N == 3:
                    board[i][j] = 1
                continue
    return board


if __name__ == "__main__":
    matrix = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print(gameOfLife(matrix))


# Runtime: 36 ms, faster than 64.39% of Python3 online submissions for Game of Life.
# Memory Usage: 13.9 MB, less than 28.88% of Python3 online submissions for Game of Life.
