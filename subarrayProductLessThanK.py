class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        res = 0
        index = 0
        maxproduct = 1
        while start < len(nums) and nums[start] > k:
            start += 1
        if start > 0 and start < len(nums):
            maxproduct = nums[start]
            res = 1
            index = start + 1
        while index < len(nums):
            if nums[index] >= k:
                start = index + 1
                maxproduct = 1
            else:
                curproduct = maxproduct * nums[index]
                while curproduct >= k:
                    curproduct = curproduct / nums[start]
                    start += 1
                res += index - start + 1
                maxproduct = curproduct
            index += 1
        return res
