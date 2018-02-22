class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        summary = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            summary[s[right]] = summary.get(s[right], 0) + 1
            while left < len(s) and len(summary) > k:
                summary[s[left]] = summary.get(s[left], 0) - 1
                if summary[s[left]] == 0:
                    del summary[s[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1
            
        return res