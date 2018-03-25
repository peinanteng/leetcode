class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], 0, res)
        return res
    
    def dfs(self, nums, cur, startIndex, res):
        if startIndex == len(nums):
            res.append(cur)
            return
        self.dfs(nums, cur, startIndex + 1, res)
        self.dfs(nums, cur + [nums[startIndex]], startIndex + 1, res)

