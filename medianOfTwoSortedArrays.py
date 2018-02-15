class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.helper(nums1, nums2, (l - 1)// 2)
        else:
            return (self.helper(nums1, nums2, (l // 2 - 1)) + self.helper(nums1, nums2, (l // 2))) / 2.
        
    def helper(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        i1, i2 = len(nums1) // 2, len(nums2) // 2
        n1, n2 = nums1[i1], nums2[i2]
        
        if i1 + i2 < k:
            if n1 > n2:
                return self.helper(nums1, nums2[i2 + 1:], k - i2 - 1)
            else:
                return self.helper(nums1[i1 + 1:], nums2, k - i1 - 1)
        else:
            if n1 > n2:
                return self.helper(nums1[:i1], nums2, k)
            else:
                return self.helper(nums1, nums2[:i2], k)
        
   