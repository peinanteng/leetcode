class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
    
        res = []
        summary = {}
        for index, word in enumerate(words):
            summary[word] = index
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                if tmp1[::-1] in summary and summary[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    res.append([i, summary[tmp1[::-1]]])
                if j > 0 and tmp2[::-1] in summary and summary[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    res.append([summary[tmp2[::-1]], i])
        return res
