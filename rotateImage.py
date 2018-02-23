class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        top = 0
        bottom = len(matrix) - 1
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1
        for x in range(len(matrix) - 1):
            y = x + 1
            while y < len(matrix[0]):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
                y += 1
