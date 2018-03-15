class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char not in '+-*/':
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                elif char == '/':
                    stack.append(int(num1 * 1.0 / num2))
        return stack[0]
