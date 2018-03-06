class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res = 0
        stack = []
        inputArray = input.split("\n")
        for i in range(len(inputArray)):
            j = 0
            count = 0
            while j < len(inputArray[i]) and inputArray[i][j] == "\t":
                count += 1
                j += 1
            if count >= len(stack):
                stack.append(len(inputArray[i]) - j)
            else:
                while count < len(stack):
                    stack.pop()
                stack.append(len(inputArray[i]) - j)
            j = 0
            while j < len(inputArray[i]) and inputArray[i][j] != '.':
                j += 1
            if j < len(inputArray[i]) - 1: 
                res = max(res, sum(stack) + len(stack) - 1)
        return res
