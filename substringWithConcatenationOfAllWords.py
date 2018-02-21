class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not s or not words or not words[0]:
            return []
        summary = {}
        for word in words:
            summary[word] = summary.get(word, 0) + 1
        lenwords = len(words) * len(words[0])
        lenword = len(words[0])
        i = 0
        while i <= len(s) - lenwords:
            flag = self.helper(s[i : i + lenwords], summary, lenword)
            if flag == 1:
                res.append(i)
            i += 1
        return res
    def helper(self, s, summary, lenword):
        newsummary = {}
        i = 0
        while i < len(s):
            if s[i :i + lenword] not in summary:
                return -1
            newsummary[s[i: i + lenword]] = newsummary.get(s[i: i + lenword], 0) + 1
            i += lenword
        for word in newsummary:
            if newsummary[word] != summary[word]:
                return -1
        return 1
        

