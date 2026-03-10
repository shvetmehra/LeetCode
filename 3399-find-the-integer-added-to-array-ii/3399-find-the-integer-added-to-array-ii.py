class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        # We only need to check these 3 possible differences
        candidates = [nums2[0] - nums1[0], nums2[0] - nums1[1], nums2[0] - nums1[2]]
        candidates.sort() # We want the minimum x, so check smallest first
        
        for x in candidates:
            if self.isValid(nums1, nums2, x):
                return x
        return 0

    def isValid(self, nums1, nums2, x):
        count_removed = 0
        i = 0 # pointer for nums1
        j = 0 # pointer for nums2
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] + x == nums2[j]:
                j += 1
            else:
                count_removed += 1
            i += 1
            
        # We are valid if we used all of nums2 and removed at most 2 from nums1
        return j == len(nums2)