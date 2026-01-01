class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        for n in nums1:
            map1[n] = True
        
        map2 = {}
        for n in nums2:
            map2[n] = True
        
        ans = []
        for n in map1:
            if n in map2:
                ans.append(n)
        
        return ans
        