class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        if left > right:
            return res
        leftHeight, rightHeight = height[left], height[right]
        while left < right:
            if leftHeight < rightHeight:
                left += 1
                if leftHeight > height[left]:
                    res += leftHeight - height[left]
                else:
                    leftHeight = height[left]
            else:
                right -= 1
                if rightHeight > height[right]:
                    res += rightHeight - height[right]
                else:
                    rightHeight = height[right]
        return res
