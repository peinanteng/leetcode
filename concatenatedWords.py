class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_set = set(words)
        res = []
        for word in words:
            if self.helper(word, 0, word_set):
                res.append(word)
        return res

    def helper(self, word, cnt, summary):
        if len(word) == 0:
            return True if cnt > 1 else False
        for i in range(len(word)):
            if word[: i + 1] in summary:
                if self.helper(word[i + 1:], cnt + 1, summary):
                    return True
        return False
