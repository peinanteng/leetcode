class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        tail = 1
        prePre, pre = nums[0], nums[1]
        for i in range(2, len(nums)):
            if nums[i] == prePre and nums[i] == pre:
                continue
            tail += 1
            prePre, pre = pre, nums[i]
            nums[tail], nums[i] = nums[i], nums[tail]
        return tail + 1
        
