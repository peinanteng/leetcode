class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        summary = {}
        start = end = res = 0
        while end < len(s):
            if s[end] not in summary:
                summary[s[end]] = end
            else:
                while start < end and s[start] != s[end]:
                    del summary[s[start]]
                    start += 1
                summary[s[start]] = end
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res