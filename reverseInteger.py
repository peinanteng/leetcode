class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
        x = abs(x)
        res = 0
        while x > 0:
            cur_digit = x % 10
            res = res * 10 + cur_digit
            x = x // 10
            if res > 2 ** 31:
                return 0
        return res * flag