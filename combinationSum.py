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
    def helper(self, nums, target, curNums, startIndex):
        if target < 0:
            return
        if target == 0:
            self.res.append(curNums)
            return
        for i in range(startIndex, len(nums)):
            self.helper(nums, target - nums[i], curNums + [nums[i]], i)
                
            
        
        
