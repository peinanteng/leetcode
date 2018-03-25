from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        queue = deque([])
        m, n = len(board), len(board[0])
        y = [0, n - 1]
        for x in range(m):
            for i in range(2):
                if board[x][y[i]] == 'O':
                    board[x][y[i]] = 'W'
                    queue.append((x, y[i]))
        x = [0, m - 1]
        for y in range(1, n - 1):
            for i in range(2):
                if board[x[i]][y] == 'O':
                    board[x[i]][y] = 'W'
                    queue.append((x[i], y))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                newX, newY = x + dx[i], y + dy[i]
                if newX >= 0 and newX < m and newY >= 0 and newY < n and board[newX][newY] == 'O':
                    board[newX][newY] = 'W'
                    queue.append((newX, newY))
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'W':
                    board[x][y] = 'O'

                
