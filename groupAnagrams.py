class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        self.res = []
        summary = {}
        for char in strs:
            temp = self.summarise(char)
            summary[temp] = summary.get(temp, []) + [char]
        for item in summary.values():
            self.res.append(item)
        return self.res
    def summarise(self, char):
        array = [0] * 26
        for c in char:
            array[ord(c) - ord('a')] += 1
        return tuple(array)
        
