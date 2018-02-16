class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                            l += 1
                    l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif s < 0:
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                            l += 1
                    l += 1
                else:
                    while r > 0 and nums[r] == nums[r - 1]:
                            r -= 1
                    r -= 1
        return res