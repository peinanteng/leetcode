class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.helper(nums, [], 0, res)
        return res
    
    def helper(self, nums, cur, startIndex, res):
        if startIndex == len(nums):
            res.append(cur)
            return
        i = startIndex + 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        self.helper(nums, cur, i, res)
        self.helper(nums, cur + [nums[startIndex]], startIndex + 1, res)
