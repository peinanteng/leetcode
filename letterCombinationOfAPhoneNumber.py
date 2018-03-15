class Solution(object):
    def letterCombinations(self, digits):
       """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for digit in digits:
            newRes = [y + x for x in phone[int(digit)] for y in res]
            res = newRes
        return res 
