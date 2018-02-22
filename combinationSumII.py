class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.helper(candidates, target, [], 0)
        return self.res
    def helper(self, nums, target, curpath, startIndex):
        if target == 0:
            self.res.append(curpath)
            return
        if target < 0 or startIndex >= len(nums):
            return
        i = startIndex + 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        self.helper(nums, target - nums[startIndex], curpath + [nums[startIndex]], startIndex + 1)
        self.helper(nums, target, curpath, i)
