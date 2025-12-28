class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        left = 0
        right = 0
        zeroCount = 0
        n = len(nums)

        while right<n:
            if nums[right]==0:
                zeroCount +=1
            if zeroCount>k:
                if nums[left]==0:
                    zeroCount -=1
                left +=1    
            if zeroCount<=k:
                ans = max(ans, right-left+1)
            right +=1
        return ans