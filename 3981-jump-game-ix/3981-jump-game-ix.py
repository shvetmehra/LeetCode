class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tempmin = [0] * (n+1)
        tempmin[n]=float("inf")
        for i in range(n-1,-1,-1):
            tempmin[i] = min(nums[i],tempmin[i+1])
        ans = [0]*n
        l=0
        while l<n:
            r=l
            nummax = nums[l]
            while r+1<n and nummax>tempmin[r+1]:
                r+=1
                nummax = max(nummax, nums[r])
            for i in range(l,r+1):
                ans[i] =  nummax
            l = r+1
        return ans
        