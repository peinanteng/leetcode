class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        while top < bottom and left < right:
            x, y = top, left
            while y <= right:
                matrix[x][y] = num
                y += 1
                num += 1
            top += 1
            x += 1
            y -= 1
            while x <= bottom:
                matrix[x][y] = num
                x += 1
                num += 1
            right -= 1
            y -= 1
            x -= 1
            while y >= left:
                matrix[x][y] = num
                y -= 1
                num += 1
            bottom -= 1
            x -= 1
            y += 1
            while x >= top:
                matrix[x][y] = num
                x -= 1
                num += 1
            left += 1
        if num <= n ** 2:
            matrix[top][left] = num
        return matrix
