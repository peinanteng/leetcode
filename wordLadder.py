class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        summary = {}
        for word in wordList:
            for i in range(len(word)):
                pre = word[:i] + '_' + word[i + 1:]
                summary[pre] = summary.get(pre, []) + [word]
        q = []
        visited = {}
        q.append((beginWord, 1))
        path = 0
        while q:
            cur, path = q.pop(0)
            for i in range(len(cur)):
                pre = cur[:i] + '_' + cur[i + 1:]
                if pre in summary and summary[pre] > 1:
                    for nei in summary[pre]:
                        if nei != cur and nei not in visited:
                            if nei == endWord:
                                return path + 1
                            q.append((nei, path + 1))
                            visited[nei] = True
        return 0
