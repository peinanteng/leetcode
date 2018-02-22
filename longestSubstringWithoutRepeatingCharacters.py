class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        summary = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            if s[right] not in summary:
                summary[s[right]] = right
                right += 1
            else:
                res = max(res, right - left)
                left = max(left, summary[s[right]] + 1)
                summary[s[right]] = right
                right += 1
        res = max(res, right - left)
        return res