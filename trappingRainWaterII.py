from heapq import heappush, heappop
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        for i in range(m):
            heappush(min_heap, (heightMap[i][0], i, 0))
            visited[i][0] = True
            heappush(min_heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][n - 1] = True
        for j in range(n):
            heappush(min_heap, (heightMap[0][j], 0, j))
            visited[0][j] = True
            heappush(min_heap, (heightMap[m - 1][j], m - 1, j))
            visited[m - 1][j] = True
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        water = 0
        while min_heap:
            h, x, y= heappop(min_heap)
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and visited[new_x][new_y] == False:
                    visited[new_x][new_y] = True
                    new_height = max(h, heightMap[new_x][new_y])
                    heappush(min_heap, (new_height, new_x, new_y, ))
                    if h > heightMap[new_x][new_y]:
                        water += h - heightMap[new_x][new_y]
        return water
