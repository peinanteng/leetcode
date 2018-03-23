        res = []
        for i in range(len(num)):
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
            self.helper(sum + int(num[:i + 1]), int(num[:i + 1]), cur + '+' + num[:i + 1], num[i + 1:], target, res)
            self.helper(sum - int(num[:i + 1]), -int(num[:i + 1]), cur + '-' + num[:i + 1], num[i + 1:], target, res)
            self.helper(sum - lastFactor + lastFactor * int(num[:i + 1]), lastFactor * int(num[:i + 1]), cur + '*' + num[:i + 1], num[i + 1:], target, res)
