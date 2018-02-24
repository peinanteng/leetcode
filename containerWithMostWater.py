class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initilise the result value
        res = 0
        # if the array contains less than 2 numbers: input is invalid
        if len(height) <= 1:
            return res
        # use two pointer, one starting from left, one starting from right
        leftp, rightp = 0, len(height) - 1
        # loop if left pointer index is less than right pointer index
        while leftp < rightp:
            # update the result if current area is larger than last result
            res = max(res, min(height[leftp], height[rightp]) * (rightp - leftp))
            # update the pointer, move the pointer whose height is lower
            if height[leftp] <= height[rightp]:
                leftp += 1
            else:
                rightp -= 1
        return res