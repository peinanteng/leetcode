class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        top, bottom = 0, len(matrix) - 1
        while top + 1 < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] < target:
                top = mid
            elif matrix[mid][0] == target:
                return True
            else:
                bottom = mid
        if matrix[top][0] > target:
            return False
        if matrix[top][0] == target or matrix[bottom][0] == target:
            return True
        if matrix[bottom][0] < target:
            top = bottom
        left, right = 0, len(matrix[top]) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[top][mid] < target:
                left = mid
            elif matrix[top][mid] > target:
                right = mid
            else:
                return True
        if matrix[top][left] == target or matrix[top][right] == target:
            return True
        return False