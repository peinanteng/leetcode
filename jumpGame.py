class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        jump = 1
        for index in range(len(nums) - 2, -1, -1):
            if index == 0 and nums[index] < jump:
                return False
            if nums[index] >= jump:
                jump = 1
            elif nums[index] < jump:
                jump += 1
        return True  
