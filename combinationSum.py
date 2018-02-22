class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    # def combinationSum(self, candidates, target):
        self.res = []
        candidates.sort()
        self.helper(candidates, target, [], 0)
        return self.res
    def helper(self, nums, target, curNums, index):
        if target < 0 or index >= len(nums):
            return
        if target == 0:
            self.res.append(curNums)
            return
        self.helper(nums, target - nums[index], curNums + [nums[index]], index)
        self.helper(nums, target, curNums, index + 1)
                
            
        
        
