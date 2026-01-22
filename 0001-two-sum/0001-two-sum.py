class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        n = len(nums)

        for i in range (n):
            rem = target - nums[i]

            if rem in dict1:
                return [dict1[rem],i]
            else:
                dict1[nums[i]]=i
