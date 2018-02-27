class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curSum = result = nums[0]
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            result = max(result, curSum)
        return result
