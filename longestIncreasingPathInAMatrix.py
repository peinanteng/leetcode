class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        ans = 0
        m, n = len(matrix), len(matrix[0])
        path = [[1] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.helper(matrix, path, visited, i, j)
                ans = max(ans, path[i][j])
        return ans
    def helper(self, matrix, path, visited, i, j):
        if visited[i][j]:
            return
        m, n = len(matrix), len(matrix[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x >= 0 and x < m and y >= 0 and y < n and matrix[i][j] > matrix[x][y]:
                if not visited[i][j]:
                    self.helper(matrix, path, visited, x, y)
                path[i][j] = max(path[i][j], path[x][y] + 1)
        visited[i][j] = True
