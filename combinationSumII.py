class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # define result
        self.res = []
        # sort the candidate numbers
        candidates.sort()
        self.helper(candidates, target, [], 0)
        return self.res
    def helper(self, nums, target, curpath, startIndex):
        # if target is 0, curpath is valid
        if target == 0:
            self.res.append(curpath)
            return
        # if target is less than 0 or startIndex larger than num length, invalid curpath
        if target < 0 or startIndex >= len(nums):
            return
        # find the next valid index
        nextIndex = startIndex + 1
        while nextIndex < len(nums) and nums[nextIndex] == nums[nextIndex - 1]:
            nextIndex += 1
        # add the current number in the path, next index to select is startIndex + 1
        self.helper(nums, target - nums[startIndex], curpath + [nums[startIndex]], startIndex + 1)
        # if skip the current number, next index is i
        self.helper(nums, target, curpath, nextIndex)
