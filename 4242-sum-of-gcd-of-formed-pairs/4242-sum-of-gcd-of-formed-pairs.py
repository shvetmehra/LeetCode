class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = []
        prefixMax = -inf
        for i in nums:
            prefixMax = max(prefixMax, i)
            mx.append(prefixMax)
        prefixGCD = [gcd(x,y) for x, y in zip(nums, mx)]
        prefixGCD.sort()

        ans = 0
        left, right = 0, n-1
        while left<right:
            ans +=gcd(prefixGCD[left], prefixGCD[right])
            left +=1
            right -=1
        return ans