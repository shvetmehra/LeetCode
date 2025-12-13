class Solution(object):
    def merge(self, left, right):
        i = j = 0
        merged = []
        while i<len(left) and j<len(right):
            if left[i]<= right[j]:
                merged.append(left[i])
                i+=1
            elif left[i]>=right[j]:
                merged.append(right[j])
                j+=1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged   
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
        