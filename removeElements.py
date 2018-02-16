class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        newtail = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newtail] = nums[i]
                newtail += 1
        return newtail