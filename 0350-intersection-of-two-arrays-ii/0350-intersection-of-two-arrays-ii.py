class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        for n in nums1:
            map1[n]= map1.get(n, 0)+1
        ans = []
        for n in nums2:
            if n in map1 and map1[n]>0:
                ans.append(n)
                map1[n]-=1
        return ans
                

        map2 = {}
        for n in nums2:
            map2[n]=True
        
        ans = []

        for n in map1:
            if n in map2:
                ans.append(n)
        for n in map2:
            if n in map1:
                ans.append(n)
           
        return (ans)
        