from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2)-self.solve(num1-1)
        
    def solve(self, num):
        if num<100:
            return 0
        s = str(num)
        @cache
        def dfs(i, lastDigit, lastComp, waves, isTight, isStarted):
            if i == len(s):
                return waves, 1

            limit = int(s[i] if isTight else 9)
            totalWaves = 0
            totalNums = 0
            
            for d in range (limit+1):
                nextTight = isTight and (d == limit)
                if not isStarted:
                    nextStarted = (d>0)
                    w, count = dfs(i+1, d, 0, 0, nextTight, nextStarted)
                    totalWaves +=w
                    totalNums +=count
                else:
                    if d>lastDigit:
                        currentComp = 1
                    elif d<lastDigit:
                        currentComp =-1
                    else: 
                        currentComp = 0
                    wavesFormed = 1 if (lastComp !=0 and currentComp == -lastComp) else 0
                    w, count = dfs(i+1, d, currentComp, waves +wavesFormed, nextTight, True)
                    totalWaves +=w
                    totalNums +=count
            return totalWaves, totalNums
        totalWavesSum, _ = dfs(0, -1, 0,0,True, False)
        return totalWavesSum