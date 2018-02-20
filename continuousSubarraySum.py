class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if k < 0:
            k = k * -1
        if k == 1:
            return True
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False
        
        
        summary = {}
        cursum = nums[0]
        summary[nums[0] % k] = 0
        for i in range(1, len(nums)):
            cursum += nums[i]
            mod = cursum % k
            if cursum % k in summary:
                if i - summary[cursum % k] > 1:
                    return True
            else:
                summary[cursum % k] = i
                if cursum % k == 0:
                    return True
        return False
        
        
                
            
        
        
