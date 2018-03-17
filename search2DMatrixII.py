class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return False
        row, column = len(matrix) - 1, 0
        ans = 0
        while row >= 0 and column < len(matrix[0]):
            if matrix[row][column] == target:
                ans += 1
                row -= 1
                column += 1
            elif matrix[row][column] < target:
                column += 1
            else:
                row -= 1
        return ans > 0
