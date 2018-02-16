class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        dividend = 1
        temp = x
        while temp > 0:
            dividend *= 10
            temp = temp // 10
        temp = x
        dividend = dividend // 10
        while temp > 0:
            front_digit = temp // dividend
            last_digit = temp % 10
            if front_digit != last_digit:
                return False
            temp = temp % dividend
            temp = temp // 10
            dividend = dividend // 100
        return True
            
            