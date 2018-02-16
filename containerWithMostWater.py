class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftp, rightp = 0, len(height) - 1
        res = 0
        while leftp + 1 < rightp:
            curwater = min(height[leftp], height[rightp]) * (rightp - leftp)
            res = max(curwater, res)
            if height[leftp] <= height[rightp]:
                leftp += 1
            else:
                rightp -= 1
        if leftp < rightp:
            curwater = min(height[leftp], height[rightp]) * (rightp - leftp)
            res = max(curwater, res)
        return res