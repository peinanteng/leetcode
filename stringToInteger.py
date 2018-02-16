class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        flag = 0
        index = 0
        while index < len(str):
            if str[index] == ' ':
                if flag != 0:
                    return res
                index += 1
            elif str[index] == '-':
                if flag == 0:
                    flag = -1
                else:
                    return res
                index += 1
            elif str[index] == '+':
                if flag == 0:
                    flag = 1
                else:
                    return res
                index += 1
            elif str[index] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return res
            else:
                break
        if flag == 0:
            flag = 1
        while index < len(str):
            if str[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                cur_digit = int(str[index])
                res = res * 10 + cur_digit
                if flag == 1 and res > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                elif flag == -1 and res > 2 ** 31:
                    return - 2 ** 31
                index += 1
            else:
                break
        return res * flag