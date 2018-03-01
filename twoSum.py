class Solution:
# this function returns the index of two integer whose sum equal to target
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1


ans = Solution().twoSum([1, 2, 3], 5)

