class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftEmpty = i==0 or flowerbed[i-1]==0
                rightEmpty = i==(len(flowerbed)-1) or flowerbed[i+1]==0
                if leftEmpty == True and rightEmpty == True:
                    flowerbed[i]=1
                    n-=1
                if n==0:
                    return True
        return False
                

            
        