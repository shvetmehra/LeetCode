class Solution:
    def rotatedDigits(self, n: int) -> int:
        count= 0
        for i in range (1, n+1):
            # invalid = False
            valid = False
            nums = i
            while nums>0:
                ans = nums%10
                if ans in [3,4,7]:
                    valid = False
                    break
                if ans in [2,5,6,9]:
                    valid = True

                nums = nums//10
            if valid:
                count +=1
        return count