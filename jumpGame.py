class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        if len(nums) == 2:
            return True if nums[-2] >= 1 else False
        if nums[0] == 0:
            return False
        for i in range(1, nums[0] + 1):
            if self.canJump(nums[i:]) == True:
                return True
        return False
        
