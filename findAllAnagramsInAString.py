class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(p) == 0 or len(s) == 0 or len(p) > len(s):
            return res
        summary = {};
        for index in range(ord('a'), ord('z') + 1):
            summary[chr(index)] = index - ord('a')
        freP = [0] * 26
        freQ = [0] * 26
        for char in p:
            freP[summary[char]] += 1
        index = 0
        while index < len(p):
            freQ[summary[s[index]]] += 1
            index += 1
        if self.compare(freP, freQ):
                res.append(0)
        for index in range(1, len(s) - len(p) + 1):
            freQ[summary[s[index - 1]]] -= 1
            freQ[summary[s[index + len(p) - 1]]] += 1
            if self.compare(freP, freQ):
                res.append(index)
        return res
    
    def compare(self, nums1, nums2):
        for a, b in zip(nums1, nums2):
            if a != b:
                return False
        return True
