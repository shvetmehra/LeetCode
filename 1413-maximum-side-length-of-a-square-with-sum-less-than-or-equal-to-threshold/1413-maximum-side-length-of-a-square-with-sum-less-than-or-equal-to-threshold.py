class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        # 1. Build the 2D Prefix Sum matrix (with padding for easy math)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                prefix[r][c] = (mat[r-1][c-1] + prefix[r-1][c] + 
                               prefix[r][c-1] - prefix[r-1][c-1])

        def can_fit(k):
            # Check if any square of side k has sum <= threshold
            for r in range(k, m + 1):
                for c in range(k, n + 1):
                    # Use the 2D prefix sum formula
                    total = (prefix[r][c] - prefix[r-k][c] - 
                             prefix[r][c-k] + prefix[r-k][c-k])
                    if total <= threshold:
                        return True
            return False

        # 2. Binary Search for the maximum side length
        low, high = 1, min(m, n)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_fit(mid):
                ans = mid
                low = mid + 1 # Try to find a bigger square
            else:
                high = mid - 1 # Too expensive, look for smaller
        
        return ans        