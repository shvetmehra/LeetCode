class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        mindiff = float('inf')
        arr.sort()

        n = (len(arr))
        for i in range (n-1):
            diff =arr[i+1]-arr[i] 
            if mindiff > diff:
                mindiff=diff
        
        for i in range (n-1):
            if arr[i+1]-arr[i] == mindiff:
                result.append([arr[i], arr[i+1]])
        return result