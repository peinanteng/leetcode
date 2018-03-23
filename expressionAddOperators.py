class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        for i in range(len(num)):
            # if the num starts with 0, continue
            if i > 0 and num[0] == '0':
                continue
            self.helper(int(num[:i + 1]), int(num[:i + 1]), num[:i + 1], num[i + 1:], target, res)
        return res
        
    def helper(self, sum, lastFactor, cur, num, target, res):
        if not num and sum == target:
            res.append(cur)
            return
        for i in range(len(num)):
            if i > 0 and num[0] == '0':
                continue
            # select i digit and perform + operator
            self.helper(sum + int(num[:i + 1]), int(num[:i + 1]), cur + '+' + num[:i + 1], num[i + 1:], target, res)
            # select i digit and perform - operator
            self.helper(sum - int(num[:i + 1]), -int(num[:i + 1]), cur + '-' + num[:i + 1], num[i + 1:], target, res)
            # select i digit and perform * operator
            self.helper(sum - lastFactor + lastFactor * int(num[:i + 1]), lastFactor * int(num[:i + 1]), \
                        cur + '*' + num[:i + 1],num[i + 1:], target, res)