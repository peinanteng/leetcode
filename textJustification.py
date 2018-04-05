class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur = []
        length = 0
        for i in range(len(words)):
            if cur and len(cur) + length + len(words[i]) > maxWidth:
                j = 0
                while length < maxWidth:
                    if j >= len(cur) - 1:
                        j = 0
                    cur[j] += ' '
                    j += 1
                    length += 1
                res.append(''.join(cur))
                cur = []
                length = 0
            cur.append(words[i])
            length += len(words[i])
        length += len(cur) - 1   
        while length < maxWidth:
            cur[-1] += ' '
            length += 1
        res.append(' '.join(cur))
        return res
