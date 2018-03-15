        newSummary = {}
        res = []
        summary = self.solve({}, dict, 0)
        for key, value in summary.items():
            newSummary[value[0]] = key
        for word in dict:
            res.append(newSummary[word])
        return res

    def solve(self, summary, dictionary, times):
        for word in dictionary:
            abb = self.getAbb(word, times)
            summary[abb] = summary.get(abb, []) + [word]
        abbList = list(summary.keys())

        for abb in abbList:
            if len(summary[abb]) > 1:
                newdict = summary[abb]
                del summary[abb]
                newSummary = self.solve({}, newdict, times + 1)
                for key, value in newSummary.items():
                    summary[key] = value
        return summary
    
    def getAbb(self, word, times):
        abb = word
        if len(word) > 3:
                abb = word[:times + 1] + str(len(word) - 2 - times) + word[-1]
        return abb if len(abb) < len(word) else word
