class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        for i in range(n):
            self.dfs(n, [[0, i]])
        return self.ans
        
    def dfs(self, n, path):
        if len(path) == n:
            self.ans += 1
            return
        row = path[-1][0] + 1
        for i in range(n):
            col = i
            if self.helper(path, row, col, n):
                self.dfs(n, path + [[row, col]])
    
    def helper(self, path, row, col, n):
        for coordinate in path:
            exRow, exCol = coordinate[0], coordinate[1]
            if row == exRow or col == exCol or abs(col - exCol) == abs(row - exRow):
                return False
        return True
