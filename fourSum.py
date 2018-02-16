class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.helper(nums[i + 1: ], target - nums[i], nums[i])
        return self.res
    def helper(self, nums, target, num):
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    self.res.append([num, nums[i], nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                else:
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                
                