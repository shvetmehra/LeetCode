class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [1 if x == target else -1 for x in nums]
        prefix = [0]*(n+1)
        for i in range (n):
            prefix [i+1]=prefix[i]+arr[i]
        ans = 0
        for r in range (1, n+1):
            for l in range (r):
                if prefix[l]<prefix[r]:
                    ans +=1
        return ans