class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            return len(s) == 0
        array = [0] * (len(s) + 1)
        array[0] = 1
        maxLength = max([len(w) for w in wordDict])
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - maxLength), i):
                if s[j: i] in wordDict and array[j] == 1:
                    array[i] = 1
                    break
        return array[len(s)] == 1
        
