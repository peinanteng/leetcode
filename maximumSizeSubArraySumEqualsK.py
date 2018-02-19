class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if len(nums) == 0:
            return res
        summary = {0 : -1}
        res = 0
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum not in summary:
                summary[cursum] = i
            target = cursum - k
            if target in summary:
                res = max(res, i - summary[target])

        return res
