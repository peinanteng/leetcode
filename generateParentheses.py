class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.helper(n, 0, 0, '')
        return self.res
    def helper(self, n, left, right, curres):
        if right >= n and left >= n:
            self.res.append(curres)
        if left < n:
            self.helper(n, left + 1, right, curres + '(')
        if right < n and right < left:
            self.helper(n, left, right + 1, curres + ')')
            