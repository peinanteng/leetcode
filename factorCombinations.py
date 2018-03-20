class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []
        m = int(n ** 0.5)
        res = []
        for i in range(2, m + 1):
            if n % i == 0:
                num1 = i
                nums2 = self.helper(i, n // i)
                for res2 in nums2:
                    res.append([num1] + res2)
        return res
    
    def helper(self, startNum, num):
        if num < startNum:
            return []
        res = [[num]]
        if num < startNum * startNum:
            return res
        m = int(num ** 0.5)
        for i in range(startNum, m + 1):
            if num % i == 0:
                num1 = i
                nums2 = self.helper(i, num // i)
                for res2 in nums2:
                    res.append([num1] + res2)
        return res
        
