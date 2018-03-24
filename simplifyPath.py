class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        q = path.split('/')
        ans = []
        for s in q:
            if s:
                if s == '..':
                    if len(ans) > 0:
                        ans.pop()
                elif s != '.':
                    ans.append(s)
        return '/' + '/'.join(ans)
