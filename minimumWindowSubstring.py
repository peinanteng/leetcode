class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        summary = {}
        summaryS = {}
        for char in t:
            summary[char] = summary.get(char, 0) + 1
        for char in s:
            summaryS[char] = summaryS.get(char, 0) + 1
        if self.compare(summaryS, summary) == -1:
            return ''
        count = len(t)
        start = 0
        res = s
        for i in range(len(s)):
            if s[i] in summary and summary[s[i]] > 0:
                count -= 1
            summary[s[i]] = summary.get(s[i], 0) - 1
            if count == 0:
                while summary[s[start]] < 0:
                    summary[s[start]] += 1
                    start += 1
                if len(res) > i - start + 1:
                    res = s[start : i + 1]
        return res
    def compare(self, summaryS, summary):
        for char in summary:
            if char not in summaryS:
                return -1
            if summary[char] > summaryS[char]:
                return -1
        return 1
