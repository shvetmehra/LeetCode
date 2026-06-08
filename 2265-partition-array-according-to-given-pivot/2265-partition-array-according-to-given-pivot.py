class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        less = []
        greater = []
        mid = []
        for i in range (n):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]==pivot:
                mid.append(nums[i])
            else: 
                greater.append(nums[i])
        return less + mid + greater 
        