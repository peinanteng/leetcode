        m = len(board)
        l = int(math.sqrt(m))
        for i in range(m):
            summary = {}
            for j in range(m):
               if board[i][j] != '.':
                    summary[board[i][j]] = summary.get(board[i][j], 0) + 1
            for key, val in summary.items():
                if val > 1:
                    return False
        for j in range(m):
            summary = {}
            for i in range(m):
                if board[i][j] != '.':
                    summary[board[i][j]] = summary.get(board[i][j], 0) + 1
            for key, val in summary.items():
                if val > 1:
                    return False
        for squareX in range(l):
            for squareY in range(l):
                summary = {}
                for i in range(squareX *l , (squareX + 1) * l):
                    for j in range(squareY*l, (squareY + 1) * l):
                        if board[i][j] != '.':
                            summary[board[i][j]] = summary.get(board[i][j], 0) + 1
                for key, val in summary.items():
                    if val > 1:
                        return False
        return True
