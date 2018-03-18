class Solution(object):
    import math
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []
        res = []
        m = int(math.sqrt(n))
        for i in range(2, m + 1):
            if n % i == 0:
                num1, num2 = i, n // i
                res.append([num1, num2])
                res2 = self.getFactors(num2)
                if not res2:
                    continue
                else:
                    for list2 in res2:
                        if min(list2) >= num1:
                            res += [[num1] + list2]
        return res
        
