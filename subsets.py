class Solution():
    def Subsets(self, nums):
        self.res = []
        self.dfs(nums, [], 0)
        return self.res
    def dfs(self, nums, curpath, startIndex):
        if startIndex == len(nums):
            self.res.append(curpath)
            return
        self.dfs(nums, curpath, startIndex + 1)
        self.dfs(nums, curpath + [nums[startIndex]], startIndex + 1)

