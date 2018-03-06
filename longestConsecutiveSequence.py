class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summary = {}
        res = 0
        for num in nums:
            summary[num] = 1
        for num in summary:
            if summary[num] == 0:
                continue
            ans = 1
            j = 1
            while num + j in summary:
                ans += 1
                summary[num + j] -= 1
                j += 1
            j = -1
            while num + j in summary:
                ans += 1
                summary[num + j] -= 1
                j -= 1
            res = max(res, ans)
        return res
