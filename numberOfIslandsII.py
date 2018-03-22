class Solution(object):

    def __init__(self):
        self.father = []
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
        
    def merge(self, x, y):
        if self.father[x] == -1 or self.father[y] == -1:
            return False
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x]= root_y
            return True
        return False
                 
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # write your code here
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(m * n):
            self.father.append(-1)
        area = 0
        res = []
        for point in positions:
            num = point[0] * n + point[1]
            if self.father[num] == -1:
                self.father[num] = num
                area += 1
            for i in range(4):
                x = point[0] + dx[i]
                y = point[1] + dy[i]
                if x >= 0 and x < m and y >= 0 and y < n and self.merge(x * n + y, num):
                    area -= 1
            res.append(area)
        return res
