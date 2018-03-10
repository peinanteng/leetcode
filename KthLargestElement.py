class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, k)
    
    def quickSelect(self, nums, k):
        left, right = -1, len(nums)
        pivot = nums[right // 2]
        i = 0
        while i < right:
            if nums[i] > pivot:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
            elif nums[i] < pivot:
                right -= 1
                nums[right], nums[i] = nums[i], nums[right]
            else:
                i += 1
        if left >= k - 1:
            return self.quickSelect(nums[:left + 1], k)
        elif right <=  k - 1:
            return self.quickSelect(nums[right:], k - right)
        else:
            return nums[k - 1]
