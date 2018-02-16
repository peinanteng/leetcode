class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if dividend < 0:
            flag = -1
        if divisor < 0:
            flag *= -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        tempdivisor = divisor
        divflag = 1
        res = 0
        while tempdivisor <= dividend:
            tempdivisor *= 10
            divflag *= 10
        
        tempdivisor /= 10
        divflag /= 10
        while dividend >= tempdivisor:
            if tempdivisor == 0 or dividend == 0:
                break
            tempres = 0
            while tempdivisor <= dividend:
                dividend -= tempdivisor
                tempres += 1
            res += tempres * divflag
            while tempdivisor > dividend:
                tempdivisor /= 10
                divflag /= 10
        
            
        return min(max(-2147483648, res * flag), 2147483647)
        
        