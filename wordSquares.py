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
        str = ''
        for word in cur:
            str += word[row]
        if str in summary:
            for word in summary[str]:
                self.dfs(summary, cur + [word], res, row + 1)
