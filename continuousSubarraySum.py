class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # this problem tries to identify whether there is a subarray in the input numbers containing at least two numbers, whose sum is the multiple of k
        # if there is 0 or 1 input number, cannot find the subarray
        if len(nums) < 2:
            return False
        # if k is less than k, mark k as -k
        if k < 0:
            k = k * -1
        # if k is 1 or -1, return True
        if k == 1:
            return True
        # if k is 0, identify whether there is two continuous zeros in input numbers
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == 0 and nums[i - 1] == 0:
                    return True
            return False
        
        # define a hash to record the sum till this number mod k
        summary = {}
        # define cursum to denote the sum till this number, initilise it as nums[0]
        cursum = nums[0]
        # initilise the hash to record the index of num[0] % k
        summary[nums[0] % k] = 0
        
        for i in range(1, len(nums)):
            # for each number, update the sum until this number
            cursum += nums[i]
            mod = cursum % k
            # if the mod in hash, means the sum of numbers starting from the index until present index is multiple of k, return True
            if cursum % k in summary:
                if i - summary[cursum % k] > 1:
                    return True
            # if the mod not in hash, put the mod in the hash, if the mod is 0, means the sum of numbers until the index is multiple of k, return True
            else:
                summary[cursum % k] = i
                if cursum % k == 0:
                    return True
        # if not finding any subarray, return False
        return False
        
        
                
            
        
        
