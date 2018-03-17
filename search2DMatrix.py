class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        column = 0
        up = 0
        down = len(matrix) - 1
        while up + 1 < down:
            mid = (up + down) // 2
            if matrix[mid][0] < target:
                up = mid
            elif matrix[mid][0] == target:
                return True
            else:
                down = mid
        if matrix[up][0] > target:
            return False
        if matrix[up][0] == target or matrix[down][0] == target:
            return True
        if matrix[down][0] < target:
            up = down
        left, right = 0, len(matrix[up]) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[up][mid] < target:
                left = mid
            elif matrix[up][mid] > target:
                right = mid
            else:
                return True
        if matrix[up][left] == target or matrix[up][right] == target:
            return True
        return False
