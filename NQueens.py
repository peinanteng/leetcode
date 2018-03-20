class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        for i in range(n):
            self.dfs(n, [[0, i]], res)
        result = []
        for path in res:
            path.sort(key=lambda coordinate: coordinate[0])
            curPath = []
            for i in range(len(path)):
                string = ''
                j = 0
                while j < path[i][1]:
                    string += '.'
                    j += 1
                string += 'Q'
                j += 1
                while j < n:
                    string += '.'
                    j += 1
                curPath += [string]
            result += [curPath]
        
        return result
        
    def dfs(self, n, path, res):
        if len(path) == n:
            res.append(path)
            return
        row = path[-1][0] + 1
        for i in range(n):
            col = i
            if self.helper(path, row, col, n):
                self.dfs(n, path + [[row, col]], res)
    
    def helper(self, path, row, col, n):
        for coordinate in path:
            exRow, exCol = coordinate[0], coordinate[1]
            if row == exRow or col == exCol or abs(col - exCol) == abs(row - exRow):
                return False
        return True
        
