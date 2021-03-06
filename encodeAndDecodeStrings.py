class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        string = ''
        for s in strs:
            for char in s:
                if char == ":":
                    string += "::"
                elif char == ";":
                    string += ";;"
                else:
                    string += char
            string += ":;"
        return string
        
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strings = []
        i, curString = 0, ""
        while i < len(s) - 1:
            if s[i : i + 2] == "::":
                curString += ":"
                i += 2
            elif s[i : i + 2] == ";;":
                curString += ";"
                i += 2
            elif s[i : i + 2] == ":;":
                strings.append(curString)
                curString = ""
                i += 2
            else:
                curString += s[i]
                i += 1
        return strings
        
