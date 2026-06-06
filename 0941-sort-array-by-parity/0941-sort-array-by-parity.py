class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = []
        odd = []
        for i in range (0, n):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even + odd
