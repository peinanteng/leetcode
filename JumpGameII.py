class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import deque
        dq = deque([(0,0)])
        while dq:
            item = dq.popleft()
            startIndex, s = item[0], item[1]
            i = startIndex + 1
            if dq:
                lastItem = dq.pop()
                i = lastItem[0] + 1
                dq.append(lastItem)
            while i < len(nums) and i <= startIndex + nums[startIndex]:
                dq.append((i, s + 1))
                i += 1
                
        return s
                
