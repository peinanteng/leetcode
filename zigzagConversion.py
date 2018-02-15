class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s
        L = [''] * numRows
        index = 0
        step = 1
        
        for char in s:
            L[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)
        
        if numRows == 1 or numRows >= len(s):
            return s
