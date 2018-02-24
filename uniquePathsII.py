class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0] * n for i in range(m)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        x, y = 0, 0
        matrix[x][y] = 1
        y += 1
        while y < n:
            if obstacleGrid[x][y] == 0:
                matrix[x][y] = matrix[x][y - 1]
            y += 1
        x, y = 1, 0
        while x < m:
            if obstacleGrid[x][y] == 0:
                matrix[x][y] = matrix[x - 1][y]
            x += 1
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 0:
                    matrix[x][y] = matrix[x - 1][y] + matrix[x][y - 1]
        return matrix[m - 1][n - 1]
