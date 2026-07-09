class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        x = [0]*n
        y = 0
        ans = []
        for i in range (1,n):
            if nums[i]-nums[i-1]>maxDiff:
                y+=1
            x[i]=y
        for u,v in queries:
            ans.append(x[u]==x[v])
        return ans