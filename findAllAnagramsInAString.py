class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        summary = {'a': 0, 'b': 1, 'c': 2, 
                   'd': 3, 'e': 4, 'f': 5, 
                   'g': 6, 'h': 7, 'i': 8, 
                   'j': 9, 'k': 10, 'l': 11,
                   'm': 12, 'n': 13, 'o': 14,
                   'p': 15, 'q': 16, 'r': 17,
                   's': 18, 't': 19, 'u': 20,
                   'v': 21, 'w': 22, 'x': 23,
                   'y': 24, 'z': 25
                  }
        res = []
        if len(p) == 0 or len(s) == 0 or len(p) > len(s):
            return res
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
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True
            
