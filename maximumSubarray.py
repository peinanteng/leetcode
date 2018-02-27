class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cursum = nums[0]
        result = nums[0]
        for num in nums[1:]:
            cursum = max(cursum + num, num)
            result = max(result, cursum)
        return result
