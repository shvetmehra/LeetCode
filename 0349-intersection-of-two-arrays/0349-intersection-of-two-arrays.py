class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        res = set()
        while i<m and j<n:
            if nums1[i]==nums2[j]:
                res.add(nums1[i])
                i +=1
                j +=1
            elif nums1[i]<nums2[j]:
                i+=1
            else: 
                j+=1
        return list(res)
        