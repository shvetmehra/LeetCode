class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []  
        def backtrack(start_num, current_path, current_sum):
            # 1. Base Case: If we found k numbers
            if len(current_path) == k:
                # If the sum matches our target, add to results
                if current_sum == n:
                    ans.append(list(current_path)) # Use list() to make a copy
                return # Stop this branch
            
            # 2. Optimization: If sum already exceeds n, stop early
            if current_sum > n:
                return
            
            # 3. Explore: Try numbers from start_num up to 9
            for i in range(start_num, 10):
                # Action: Add the number
                current_path.append(i)
                
                # Recursion: Move to the next number (i + 1)
                backtrack(i + 1, current_path, current_sum + i)
                
                # Backtrack: Remove the number to try the next possibility
                current_path.pop()

        backtrack(1, [], 0)
        return ans