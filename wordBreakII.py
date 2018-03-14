class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        summary = {}
        summary[len(s)] = ['']
        self.helper(0, s, wordDict, summary)
        return summary[0]
    
    def helper(self, i, s, wordDict, summary):
        if i not in summary:
            res = []
            for j in range(i + 1, len(s) + 1):
                if s[i : j] in wordDict:
                    restList = self.helper(j, s, wordDict, summary)
                    for word in restList:
                        res.append(s[i : j] + (word and ' ' + word))
            summary[i] = res
        return summary[i]
    