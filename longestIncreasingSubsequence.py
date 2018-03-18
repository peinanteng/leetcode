class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for cur, val in enumerate(nums):
            for i in range(cur):
                if val > nums[i]:
                    dp[cur] = max(dp[i] + 1, dp[cur])
        return max(dp)
