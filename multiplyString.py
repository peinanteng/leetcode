class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = self.strToInteger(num1)
        n2 = self.strToInteger(num2)
        
        result = self.multiply(n1, n2)
        
        return self.integerToStr(result)
    
    def strToInteger(self, str):
        stack = []
        for i in range(len(str)):
            stack.append(int(str[i]))
        res = 0
        while stack:
            res = res * 10 + stack.pop()
        return res
    
    def multiply(self, n1, n2):
        stack = []
        tempn2 = n2
        while tempn2:
            stack.append(tempn2 % 10)
            tempn2 /= 10
        res = 0
        flag = 1
        while stack:
            digit = stack.pop(0)
            tempres = 0
            while digit:
                tempres += n1
                digit -= 1
            tempres *= flag
            res += tempres
            flag = flag * 10
        return res
    
    def integerToStr(self, num):
        stack = []
        while num:
            stack.append(num % 10)
            num /= 10
        output = ''
        while stack:
            output += str(stack.pop)
        return output
