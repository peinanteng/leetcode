class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        summary = {}
        for word in words:
            for i in range(len(word)):
                summary[word[:i + 1]] = summary.get(word[:i + 1], []) + [word]
        res = []
        for word in words:
            cur = [word]
            self.dfs(summary, cur, res, 1)
        return res

    def dfs(self, summary, cur, res, row):
        if len(cur) == len(cur[0]):
            res.append(cur)
            return
        if row > len(cur[0]):
            return
        s = ''
        for word in cur:
            s += word[row]
        if s in summary:
            for word in summary[s]:
                self.dfs(summary, cur + [word], res, row + 1)