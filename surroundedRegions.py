class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        queue = []
        m, n = len(board), len(board[0])
        for x in range(m):
            if board[x][0] == 'O':
                board[x][0] = 'W'
                queue.append((x, 0))
            if board[x][n - 1] == 'O':
                board[x][n - 1] = 'W'
                queue.append((x, n - 1))

        for y in range(1, n - 1):
            if board[0][y] == 'O':
                board[0][y] = 'W'
                queue.append((0, y))
            if board[m - 1][y] == 'O':
                board[m - 1][y] = 'W'
                queue.append((m - 1, y))
        while queue:
            pair = queue.pop()
            x, y = pair[0], pair[1]
            if x > 0 and board[x - 1][y] == 'O':
                board[x-1][y] = 'W'
                queue.append((x - 1, y))
            if x < m - 1 and board[x + 1][y] == 'O':
                board[x+1][y] = 'W'
                queue.append((x + 1, y))
            if y > 0 and board[x][y - 1] == 'O':
                board[x][y-1] = 'W'
                queue.append((x, y - 1))
            if y < n - 1 and board[x][y + 1] == 'O':
                board[x][y+1] = 'W'
                queue.append((x, y + 1))
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                if board[x][y] == 'W':
                    board[x][y] = 'O'
