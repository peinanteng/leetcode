class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.helper(word, '', False, res)
        return res[::-1]
    def helper(self, word, cur, abb, res):
        if not word:
            res.append(cur)
            return
        self.helper(word[1:], cur + word[0], False, res)
        if not abb:
            for i in range(1, len(word) + 1):
                self.helper(word[i:], cur + str(i), True, res)
