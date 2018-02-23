class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while top < bottom or left < right:
            x, y = top, left
            while x <= bottom and y <= right:
                res.append(matrix[x][y])
                y += 1
            top += 1
            x, y = top, right
            while x <= bottom and y >= left:
                res.append(matrix[x][y])
                x += 1
            right -= 1
            x, y = bottom, right
            while x >= top and y >= left:
                res.append(matrix[x][y])
                y -= 1
            bottom -= 1
            x, y = bottom, left
            while x >= top and y <= right:
                res.append(matrix[x][y])
                x-= 1
            left += 1
        if len(res) < m * n:
            res.append(matrix[top][left])
        return res
