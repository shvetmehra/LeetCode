class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0]*(2*limit+2)
        for i in range(n//2):
            a = nums[i]
            b = nums[n-1-i]
            if a>b:
                a,b = b,a

            diff[2]+=2
            diff[a+1]-=1
            if b+limit+1<=2*limit:
                diff[b+limit+1]+=1
            diff[a+b]-=1
            if a+b+1<=2*limit:
                diff[a+b+1]+=1
            
        moves = 0
        minMoves = float('inf')

        for i in range (2, 2*limit+1):
            moves+=diff[i]
            minMoves = min(minMoves, moves)
        return minMoves