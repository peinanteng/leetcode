class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # the script tries to find out the sub array with minimum length whose sum is no less than s 
        if sum(nums) < s:
            return 0
        # initialise the res as the total length of nums
        res = len(nums)
        i, j = 0, 0
        # find the first window whose sum is no less than s
        while j < len(nums) and sum(nums[i : j + 1]) < s:
            j += 1
        # update the res
        res = min(res, j - i + 1)
        # continue to find the following window
        while j < len(nums):
            # the new window length should be no longer than old window
            i = j - res + 1
            # if the window sum is larger than s
            if sum(nums[i : j + 1]) >= s:
                # increase i until windown sum is less than s
                while sum(nums[i : j + 1]) >= s:
                    i += 1
                # decrease i to make the windown sum is larger than s
                i -= 1
                #  update the res
                res = min(res, j - i + 1)
            # update j
            j += 1
        return res
