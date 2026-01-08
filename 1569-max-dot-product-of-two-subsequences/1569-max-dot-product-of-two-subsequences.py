class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)

        dp = [[float('-inf')]* m for _ in range(n)]

        for i in range (n):
            for j in range (m):
                product = nums1[i]*nums2[j]

                if i>0 and j>0:
                    dp[i][j] = product+ max(0, dp[i-1][j-1])
                else:
                    dp[i][j] = product
                
                if i>0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j>0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                
                
        return dp[n-1][m-1]
        