class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end = -1, len(nums)
        i = 0
        while i < end:
            if nums[i] == 0:
                start += 1
                nums[start], nums[i] = nums[i], nums[start]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                end -= 1
                nums[end], nums[i] = nums[i], nums[end]

