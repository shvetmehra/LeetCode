class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_str = ",".join(map(str, sorted(nums))) + ","
        nums_str = ",".join(map(str, nums)) + ","
        D_nums = nums_str + nums_str
        if sorted_str in D_nums:
            return True
        else:
            return False