class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        summary = {}
        self.helper(s, wordDict, summary)
        return summary[s]

    def helper(self, s, wordDict, summary):
        if s in summary:
            return summary[s]
        res = []
        for word in wordDict:
            startIndex = self.findIndex(s, word)
            if startIndex != 0:
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                restList = self.helper(s[len(word):], wordDict, summary)
                for rest in restList:
                    res.append(word + " " + rest)
        summary[s] = res
        return res

    def findIndex(self, s, word):
        length = len(word)
        if length == 0:
            return -1
        for i in range(len(s)):
            if s[i: i + length] == word:
                return i
        return -1
