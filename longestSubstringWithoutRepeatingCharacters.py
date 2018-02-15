class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        start = 0
        curlen = 1
        maxlen = 1
        for i in range(1, len(s)):
            if s[i] not in s[start : i]:
                curlen += 1   
            else:
                while s[start] != s[i]:
                    start += 1
                start += 1
                curlen = i - start + 1
            maxlen = max(maxlen, curlen)
        return maxlen