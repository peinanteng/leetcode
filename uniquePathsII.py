class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0 or obstacleGrid[0][0] == 1:
            return 0

        matrix = [[0] * n for i in range(m)]
        matrix[0][0] = 1
        x = 0
        for y in range(1, n):
            if obstacleGrid[x][y] == 0:
                matrix[x][y] = matrix[x][y - 1]
        y = 0
        for x in range(1, m):
            if obstacleGrid[x][y] == 0:
                matrix[x][y] = matrix[x - 1][y]
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 0:
                    matrix[x][y] = matrix[x - 1][y] + matrix[x][y - 1]
        return matrix[-1][-1]
