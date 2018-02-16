class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res  = ''
        if len(s) == 0:
            return res
        res = s[0]
        maxlen = 1
        if len(s) == 0:
            return res
        for i in range(1, len(s)):
            if i - maxlen - 1 >= 0 and s[i - maxlen - 1 : i + 1] == s[i - maxlen - 1 : i + 1][::-1]:
                res = s[i - maxlen - 1 : i + 1]
                maxlen += 2
            elif i - maxlen >= 0 and s[i - maxlen : i + 1] == s[i - maxlen : i + 1][::-1]:
                res = s[i - maxlen : i + 1]
                maxlen += 1
        return res
            
      