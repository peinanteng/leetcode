class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        memo = set()
        return self.helper(stones, 1, 1, stones[-1], memo)
    
    def helper(self, stones, cur, speed, target, memo):
        if (cur, speed) in memo:
            return False
        if cur == target:
            return True
        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        memo.add((cur, speed))
        for i in range(speed - 1, speed + 2):
            if self.helper(stones, cur + i, i, target, memo):
                return True
        return False
            
