class Solution():
    def SubsetsII(self, nums):
        nums.sort()
        self.res = []
        self.dfs(nums, [], 0)
        return self.res
    def dfs(self, nums, curpath, startIndex):
        if startIndex == len(nums):
            self.res.append(curpath)
            return
        nextIndex = startIndex + 1
        while nextIndex < len(nums) and nums[nextIndex] == nums[nextIndex - 1]:
            nextIndex += 1
        self.dfs(nums, curpath + [nums[startIndex]], startIndex + 1)
        self.dfs(nums, curpath, nextIndex)

