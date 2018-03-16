class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) < 10:
            return res
        summary = {}
        for i in range(len(s) - 9):
            if s[i:i+ 10] in summary and summary[s[i:i+10]] == 1:
                    res.append(s[i:i+10])
            summary[s[i:i+10]] = summary.get(s[i:i+10], 0) + 1
        return res
