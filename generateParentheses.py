class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n, n, "", res)
        return res
    
    def helper(self, left, right, cur, res):
        if left == 0 and right == 0:
            res.append(cur)
        if left:
            self.helper(left - 1, right, cur + '(', res)
        if right > left:
            self.helper(left, right - 1, cur + ')', res)