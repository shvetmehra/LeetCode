class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        map1 = {}
        for n in nums1:
            map1[n]=True
        map2 = {}
        for n in nums2:
            map2[n]=True
        
        ans1 = []
        for n in map1:
            if n not in map2:
                ans1.append(n)
        
        ans2 = []
        for n in map2:
            if n not in map1:
                ans2.append(n)
        return [ans1, ans2]