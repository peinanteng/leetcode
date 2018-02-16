class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return res
        leftp, rightp = 0, len(height) - 1

        while leftp < rightp:
            res = max(res, min(height[leftp], height[rightp]) * (rightp - leftp))
            if height[leftp] <= height[rightp]:
                leftp += 1
            else:
                rightp -= 1
        return res