class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        string = ''
        for str in strs:
            for char in str:
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
            if s[i] == ":" and s[i + 1] == ":":
                curString += ":"
                i += 2
            elif s[i] == ";" and s[i + 1] == ";":
                curString += ";"
                i += 2
            elif s[i] == ":" and s[i + 1] == ";":
                strings.append(curString)
                curString = ""
                i += 2
            else:
                curString += s[i]
                i += 1
        return strings
        
