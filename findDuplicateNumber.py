class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(nums, mid) <= mid:
                left = mid
            else:
                right = mid
        if self.count(nums, left) <= left:
            return right
        return left
    def count(self, nums, mid):
        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1
        return cnt
