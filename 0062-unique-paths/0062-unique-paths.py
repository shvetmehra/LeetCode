class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0]*n
        for i in range (m):
            curr = [0]*n
            for j in range (n):
                if i==0 and j==0:
                    curr[0]=1
                else:
                    if i>0:
                        up = prev[j]
                    else:
                        up = 0
                    if j==0:
                        left = 0
                    else:
                        left = curr[j-1]
                    curr[j]=up+left
            prev = curr.copy()
        return prev[n-1]
        