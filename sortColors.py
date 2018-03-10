class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        front, back = -1, len(nums)
        i = 0
        while i < back:
            if nums[i] == 0:
                front += 1
                nums[front], nums[i] = nums[i], nums[front]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                back -= 1
                nums[back], nums[i] = nums[i], nums[back]

