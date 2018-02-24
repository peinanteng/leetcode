class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        matrix = [[0] * n for i in range(m)]
        
        x, y = 0, 0
        matrix[0][0] = grid[0][0]
        y = 1
        while y < n:
            matrix[x][y] = matrix[x][y - 1] + grid[x][y]
            y += 1
        x, y = 1, 0
        while x < m:
            matrix[x][y] = matrix[x - 1][y] + grid[x][y]
            x += 1
        for x in range(1, m):
            for y in range(1, n):
                matrix[x][y] = min(matrix[x - 1][y], matrix[x][y - 1]) + grid[x][y]
        return matrix[m - 1][n - 1]


