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
            string = s[i : i + 10]
            if string in summary and summary[string] == 1:
                res.append(string)
            summary[string] = summary.get(string, 0) + 1
        return res
