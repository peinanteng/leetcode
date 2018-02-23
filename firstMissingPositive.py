class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for num in nums:
            nums[num % n] += n
        i = 0
        while i < len(nums) and nums[i] >= n :
            i += 1
        return i
                
