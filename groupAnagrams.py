class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        summary = {}
        for s in strs:
            key = self.summarise(s)
            summary[key] = summary.get(key, []) + [s]
        return list(summary.values())
    
    def summarise(self, s):
        array = [0] * 26
        for c in s:
            array[ord(c) - ord('a')] += 1
        return tuple(array)
        
