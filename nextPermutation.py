class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break
        if pivot == len(nums):
            nums.reverse()
        else:
            curindex = pivot + 1
            curval = nums[pivot + 1]
            for i in range(curindex + 1, len(nums)):
                if curval >= nums[i] and nums[i] > nums[pivot]:
                    curval = nums[i]
                    curindex = i
            nums[curindex], nums[pivot] = nums[pivot], nums[curindex]
            self.partialreverse(nums, pivot + 1, len(nums) - 1)
    def partialreverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
