        res = []
        if not board or not board[0]:
            return res
        m, n = len(board), len(board[0])
        for word in words:
            i = 0
            while i < m:
                j = 0
                while j < n:
                    if board[i][j] == word[0]:
                        visited = [[False] * n for _ in range(m)]
                        if self.helper(board, word, visited, i, j):
                            if word not in res:
                                res.append(word)
                    	     i, j = m, n
                    j += 1
                i += 1
        return res
    
    def helper(self, board, word, visited, i, j):
        if len(word) == 0:
            return True
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == True or board[i][j] != word[0]:
            return False
        visited[i][j] = True
        if self.helper(board, word[1:], visited, i + 1, j) or \
        self.helper(board, word[1:], visited, i - 1, j) or \
        self.helper(board, word[1:], visited, i, j + 1) or \
        self.helper(board, word[1:], visited, i, j - 1):
            return True
        visited[i][j] = False
        return False
