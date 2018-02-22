class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        pleft, pright = -1, -1
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right -= 1
        if nums[left] == target:
            pleft = left
        elif nums[right] == target:
            pleft = right
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left += 1
        if nums[right] == target:
            pright = right
        elif nums[left] == target:
            pright = left

        return [pleft, pright]
        
