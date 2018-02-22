class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2  
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right
        return left + 1
        
        
