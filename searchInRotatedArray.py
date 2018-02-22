class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target >= nums[0]:
                if nums[mid] < target and nums[mid] >= nums[0]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] < nums[-1] and nums[mid] > target:
                    right = mid
                else:
                    left = mid
        if left >= 0 and left < len(nums) and nums[left] == target:
            return left
        if right >= 0 and right < len(nums) and nums[right] == target:
            return right
        return -1
                    
                    
