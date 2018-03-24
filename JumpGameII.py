from collections import deque
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dq = deque([(0,0)])
        while dq:
            startIndex, s = dq.popleft()
            i = startIndex + 1
            if dq:
                lastItem = dq.pop()
                i = lastItem[0] + 1
                dq.append(lastItem)
            while i < len(nums) and i <= startIndex + nums[startIndex]:
                dq.append((i, s + 1))
                i += 1
                
        return s
                
