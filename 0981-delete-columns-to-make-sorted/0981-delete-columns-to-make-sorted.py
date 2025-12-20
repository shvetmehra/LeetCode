class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = 0
        row = len(strs)
        col = len(strs[0])
        for i in range (col):
            for j in range(row-1):
                if strs[j][i]> strs[j+1][i]:
                    ans +=1
                    break
        return ans
        