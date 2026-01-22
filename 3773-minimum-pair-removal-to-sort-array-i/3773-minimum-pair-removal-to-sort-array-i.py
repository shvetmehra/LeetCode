class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        
        ops = 0
        
        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0
            
            # Find adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            
            # Replace the pair with their sum
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1
        
        return ops