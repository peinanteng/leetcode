class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        res = len(nums)
        i, j = 0, 0
        while j < len(nums) and sum(nums[i : j + 1]) < s:
            j += 1
        res = min(res, j - i + 1)
        while j < len(nums):
            i = j - res + 1
            if sum(nums[i : j + 1]) >= s:
                while sum(nums[i : j + 1]) >= s:
                    i += 1
                i -= 1
                res = min(res, j - i + 1)
            j += 1
        return res
