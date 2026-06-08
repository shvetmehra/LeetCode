class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    
        less = []
        greater = []
        mid = []
        for num in nums:
            if num<pivot:
                less.append(num)
            elif num==pivot:
                mid.append(num)
            else: 
                greater.append(num)
        return less + mid + greater 
        