class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1 = len(haystack)
        len2 = len(needle)
        lendiff = len1 - len2
        
        if lendiff == 0:
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(lendiff + 1):
            if haystack[i : i + len2] == needle:
                return i
        return -1
    
        