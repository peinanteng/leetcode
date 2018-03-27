import Queue
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        q = Queue.Queue()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.put((i, j))
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        while q.qsize():
            x, y = q.get()
            day = rooms[x][y]
            for i in range(4):
                newX, newY = x + dx[i], y + dy[i]
                if newX >= 0 and newX < m and newY >= 0 and newY < n and rooms[newX][newY] == 2147483647:
                    rooms[newX][newY] = day + 1
                    q.put((newX, newY))
        
