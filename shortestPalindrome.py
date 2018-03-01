class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 1
        for i in range(1, len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                maxLen = i + 1
        addedString = ''
        addedString = s[maxLen:][::-1]
        
        return addedString + s
