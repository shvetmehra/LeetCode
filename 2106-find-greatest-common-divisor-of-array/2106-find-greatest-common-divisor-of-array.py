import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        return math.gcd(max_num, min_num)