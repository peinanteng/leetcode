class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    table = [[False] * len(board[0]) for _ in range(len(board))]
                    if self.helper(board, word, table, "", i, j):
                        return True
        return False

    def helper(self, board, word, table, curStr, x, y):
        table[x][y] = True
        curStr += board[x][y]
        if curStr == word:
            return True
        if x < len(board) - 1 and table[x + 1][y] == False and board[x + 1][y] == word[len(curStr)]:
            if self.helper(board, word, table, curStr, x + 1, y):
                return True
        if y < len(board[0]) - 1 and table[x][y + 1] == False and board[x][y + 1] == word[len(curStr)]:
            if self.helper(board, word, table, curStr, x, y + 1):
                return True
        if x > 0 and table[x - 1][y] == False and board[x - 1][y] == word[len(curStr)]:
            if self.helper(board, word, table, curStr, x - 1, y):
                return True
        if y > 0 and table[x][y - 1] == False and board[x][y - 1] == word[len(curStr)]:
            if self.helper(board, word, table, curStr, x, y - 1):
                return True
        table[x][y] = False
        return False
