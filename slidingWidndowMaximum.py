from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dq = deque()
        if len(nums) < k or k == 0:
            return res
        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i + 1 < k:
                continue
            while dq and dq[0] <= i - k:
                dq.popleft()
            res.append(nums[dq[0]])
        return res
        
