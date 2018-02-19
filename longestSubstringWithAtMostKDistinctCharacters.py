class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        summary = {}
        start, Start, End = 0, 0, 0
        for index, char in enumerate(s, 1):
            summary[char] = summary.get(char, 0) + 1
            if len(summary) <= k:
                if End == 0 or index - start > End - Start:
                    Start, End = start, index
            else:
                while start < index and len(summary) > k:
                    summary[s[start]] -= 1
                    if summary[s[start]] == 0:
                        del summary[s[start]]
                    start += 1
                if index - start > End - Start :
                    Start, End = start, index
        return End - Start