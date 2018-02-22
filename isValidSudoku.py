class Solution(object):
    import math
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != len(board[0]):
            return False
        if self.isValidRow(board) == -1:
            return False
        if self.isValidColumn(board) == -1:
            return False
        if self.isValidSquare(board) == -1:
            return False
        return True
    def isValidRow(self, board):
        if not board:
            return -1
        length = len(board)
        rowStart = 0
        rowEnd = length
        for row in range(rowStart, rowEnd):
            summary = {}
            colStart = 0
            colEnd = length
            for column in range(colStart, colEnd):
                if board[row][column] == '.':
                    continue
                if board[row][column] in summary:
                    return -1
                else:
                    summary[board[row][column]] = 1
        return 1
    def isValidColumn(self, board):
        if not board:
            return -1
        length = len(board)
        colStart = 0
        colEnd = length
        for column in range(colStart, colEnd):
            summary = {}
            rowStart = 0
            rowEnd = length
            for row in range(rowStart, rowEnd):
                if board[row][column] == '.':
                    continue
                if board[row][column] in summary:
                    return -1
                else:
                    summary[board[row][column]] = 1
        return 1
    def isValidSquare(self, board):
        if not board:
            return -1
        length = len(board)
        n = int(math.sqrt(length))
        rowStart = 0
        colStart = 0
        rowEnd = n
        colEnd = n
        while rowStart < length and colStart < length:
            summary = {}
            for i in range(rowStart, rowEnd):
                for j in range(colStart, colEnd):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in summary:
                        return -1
                    else:
                        summary[board[i][j]] = 1
            if colEnd < length:
                colStart += n
                colEnd += n
            else:
                rowStart += n
                rowEnd += n
                colStart = 0
                colEnd = n
            
            
            
