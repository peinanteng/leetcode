class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        self.helper(nums, [])
        return self.res
    def helper(self, nums, path):
        if not nums:
            self.res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.helper(nums[:i] + nums[i + 1:], path +[nums[i]])
    
            
