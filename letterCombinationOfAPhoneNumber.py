class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        PhoneNum = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        for num in digits:
            if len(res) == 0:   
                for char in PhoneNum[int(num)]:
                    res.append(char)
            else:
                curres = []
                for char in PhoneNum[int(num)]:
                    for reschar in res:
                        reschar += char
                        curres.append(reschar)
                res = curres
        return res
        