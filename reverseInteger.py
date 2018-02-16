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
        stack = []
        while x > 0:
            digit = x % 10
            stack.append(digit)
            x = x / 10
        while stack:
            digit = stack.pop(0)
            x = x * 10 + digit
            if x > 2 ** 31:
                return 0
        return x * flag