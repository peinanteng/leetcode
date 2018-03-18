class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    import math
    def isValidSudoku(self, board):
        # write your code here
        m = len(board)
        l = int(math.sqrt(m))
        for i in range(m):
            summary = {}
            for j in range(m):
               if board[i][j] != '.':
                    if board[i][j] in summary:
                        return False
                    summary[board[i][j]] = 1
        for j in range(m):
            summary = {}
            for i in range(m):
                if board[i][j] != '.':
                    if board[i][j] in summary:
                        return False
                    summary[board[i][j]] = 1
        for squareX in range(l):
            for squareY in range(l):
                summary = {}
                for i in range(squareX * l , (squareX + 1) * l):
                    for j in range(squareY * l, (squareY + 1) * l):
                        if board[i][j] != '.':
                            if board[i][j] in summary:
                                return False
                            summary[board[i][j]] = 1
        return True