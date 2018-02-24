class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        x, y = 0, 1
        while y < n:
            grid[x][y] += grid[x][y - 1]
            y += 1
        x, y = 1, 0
        while x < m:
            grid[x][y] += grid[x - 1][y]
            x += 1
        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
        return grid[m - 1][n - 1]
