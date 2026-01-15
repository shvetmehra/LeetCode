class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        hBars.sort()
        vBars.sort()
        hMax, vMax = 1, 1
        hCurr, vCurr = 1, 1

        for i in range (1, len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                hCurr +=1
            else:
                hCurr =1
            hMax = max(hMax, hCurr)
        for i in range (1, len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                vCurr +=1
            else: 
                vCurr =1
            vMax = max(vMax, vCurr)
        side = min(hMax, vMax) +1
        return side*side
        