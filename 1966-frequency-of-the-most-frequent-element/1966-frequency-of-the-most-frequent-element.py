class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len (nums)
        left = 0
        total = 0
        ans = 1
        nums.sort()      
        for right in range (n):
            total += nums[right]
            leftOverArray = right - left+1
            actionNeeded = nums[right]*leftOverArray-total
            while actionNeeded>k:
                total -= nums[left]
                left +=1
                leftOverArray =right - left+1
                actionNeeded = nums[right]*leftOverArray-total
            ans = max(ans, right-left+1)
        return ans
                  