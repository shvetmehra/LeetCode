class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [1 if x== target else -1 for x in nums]
        prefix = [0] *(n+1)
        for i in range (n):
            prefix[i+1] = prefix[i]+arr[i]
        val = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(val)}
        bit = [0]*(len(rank)+2)
        def update(i):
            while i < len(bit):
                bit[i]+=1
                i +=i&-i
        def query(i):
            res = 0
            while i >0:
                res +=bit[i]
                i-=i&-i
            return res
        ans = 0
        for x in prefix:
            r = rank[x]
            ans +=query(r-1)
            update (r)
        return ans