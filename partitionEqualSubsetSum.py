class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or sum(nums) % 2 or max(nums) > sum(nums) // 2:
            return False
        nums.sort(reverse = True)
        summary = {}
        for i in range(len(nums)):
            if self.helper(i, nums, sum(nums) // 2, summary):
                return True
        return False
        
    def helper(self, start, nums, target, summary):
        if target < 0:
            return False
        if target == 0:
            return True
        if target not in summary:
            summary[target] = False
            for i in range(start, len(nums)):
                if self.helper(i + 1, nums, target - nums[i], summary):
                    summary[target] = True             
        return summary[target]
            
