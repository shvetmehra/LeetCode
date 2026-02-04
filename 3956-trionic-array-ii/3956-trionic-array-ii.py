class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        p1 = p2 = p3 = -float('inf')
        ans = -float('inf')
        
        for i in range(1, n):
            nxt_p1 = nxt_p2 = nxt_p3 = -float('inf')
            
            if nums[i] > nums[i-1]:
                nxt_p1 = max(nums[i] + nums[i-1], p1 + nums[i])
                nxt_p3 = max(p2 + nums[i], p3 + nums[i])
            elif nums[i] < nums[i-1]:
                nxt_p2 = max(p1 + nums[i], p2 + nums[i])
            
            p1, p2, p3 = nxt_p1, nxt_p2, nxt_p3
            ans = max(ans, p3)
            
        return int(ans)