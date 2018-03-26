class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        tail = 1
        pre, cur = nums[0], nums[1]
        for i in range(2, len(nums)):
            if nums[i] == pre and nums[i] == cur:
                continue
            tail += 1
            pre, cur = cur, nums[i]
            nums[tail], nums[i] = nums[i], nums[tail]
        return tail + 1
        
