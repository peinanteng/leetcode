class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, [])
        return self.res
    def helper(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i + 1:], path + [nums[i]])
            
