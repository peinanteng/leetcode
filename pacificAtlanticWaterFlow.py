class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        m, n = len(matrix), len(matrix[0])
        pacificVisited = [[False] * n for _ in range(m)]
        atlanticVisited = [[False] * n for _ in range(m)]
        pacificStack, atlanticStack = [], []
        for i in range(m):
            pacificStack.append((i, 0))
            atlanticStack.append((i, n - 1))
        for j in range(n):
            pacificStack.append((0, j))
            atlanticStack.append((m - 1, j))
        self.dfs(matrix, pacificStack, pacificVisited)
        self.dfs(matrix, atlanticStack, atlanticVisited)
        
        for i in range(m):
            for j in range(n):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    res.append([i, j])
        return res
    
    def dfs(self, matrix, stack, visited):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        m, n = len(matrix), len(matrix[0])
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] < matrix[x][y]:
                    continue
                stack.append((nx, ny))
