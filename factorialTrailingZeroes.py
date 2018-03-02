class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            ans += n // 5
            n = n // 5
        return ans
            
