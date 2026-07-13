class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        sample = 123456789
        min_len = len(str(low))
        max_len = len(str(high))
        for i in range(min_len, max_len+1):
            for j in range(10-i):
                substring = str(sample)[j:j+i]
                num = int(substring)
                if low<=num<=high:
                    ans.append(num)
        return ans
        