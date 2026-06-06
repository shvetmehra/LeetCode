class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        n = len(nums)
        for i in range (0,n):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        eve = od =0
        for i in range (n):
            if i%2==0:
                nums[i]=even[eve]
                eve+=1
            else:
                nums[i]=odd[od]
                od+=1
        return nums