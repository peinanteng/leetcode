class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 1
        for i in range(1, len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                maxlen = i + 1
        Addedstring = ''
        if maxlen < len(s):
            Addedstring = s[maxlen :][::-1]
        
        return Addedstring + s
