class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.helper(nums, [], res)
        return res
    
    def helper(self, nums, cur, res):
        if not nums:
            res.append(cur)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.helper(nums[:i] + nums[i + 1:], cur + [nums[i]], res)
    
            
