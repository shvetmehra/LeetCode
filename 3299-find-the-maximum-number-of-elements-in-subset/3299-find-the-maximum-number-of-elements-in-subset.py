from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = count.get(1,0)
        if ans %2 ==0 and ans>0:
            ans -=1
        for num in sorted(count.keys()):
            if num ==1:
                continue
            res = 0
            x = num
            while count[x]>=2:
                res +=2
                x*=x
            if count[x]>=1:
                res+=1
            else:
                res-=1
            ans = max(ans, res)
        return max (ans, 1)

