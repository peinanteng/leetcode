class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.helper(n, 0, 0, '')
        return self.res
    def helper(self, n, leftn, rightn, curres):
        if leftn == n and rightn == n:
            self.res.append(curres)
        if leftn < n:
            self.helper(n, leftn + 1, rightn, curres + '(')
        if rightn < leftn:
            self.helper(n, leftn, rightn + 1, curres + ')')