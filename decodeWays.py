class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        prePreCount, preCount, curCount = 1, 1, 0
        for i in range(1, len(s)):
            flag1 = self.decodeTwoDigit(s[i - 1: i + 1])
            flag2 = self.decodeDigit(s[i])
            if flag1 == 0 and flag2 == 0 :
                return 0
            elif flag1 == 0:
                curCount = preCount
            elif flag2 == 0:
                curCount = prePreCount
            else:
                curCount = preCount + prePreCount
            prePreCount, preCount = preCount, curCount
        return curCount
    
    def decodeDigit(self, digit):
        return digit != '0'
    def decodeTwoDigit(self, digit):
        return digit[0] == '1' or (digit[0] == '2' and digit[1] <= '6')
