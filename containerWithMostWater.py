class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            curArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, curArea)
            newLeft = left + 1 if height[left] <= height[right] else left
            newRight = right - 1 if height[left] > height[right] else right
            left, right = newLeft, newRight
        return maxArea
    
