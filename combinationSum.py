class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # define the result
        res = []
        # sort the numbers in the candidates array
        candidates.sort()
        self.helper(candidates, target, [], 0, res)
        return self.res
    def helper(self, nums, target, curNums, index, res):
        # if target is less than 0, curNums is invalid; if index is larger than length of input numbers, invalid selection
        if target < 0 or index >= len(nums):
            return
        # if target is 0, curNums is valid selection
        if target == 0:
            self.res.append(curNums)
            return
        # select nums[index], next number to select is still nums[index]
        self.helper(nums, target - nums[index], curNums + [nums[index]], index, res)
        # not select nums[index], next number to select is nums[index + 1]
        self.helper(nums, target, curNums, index + 1, res)
                
            
        
        
