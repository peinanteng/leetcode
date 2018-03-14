class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        matrix = [[0] * n for i in range(m)]
        x = 0
        for y in range(n):
            matrix[x][y] = 1
        y = 0
        for x in range(m):
            matrix[x][y] = 1
        
        for x in range(1, m):
            for y in range(1, n):
                matrix[x][y] = matrix[x - 1][y] + matrix[x][y - 1]
        return matrix[m - 1][n - 1]
        
