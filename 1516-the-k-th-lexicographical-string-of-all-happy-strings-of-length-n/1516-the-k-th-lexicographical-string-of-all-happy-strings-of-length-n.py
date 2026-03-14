class Solution:
    def solve(self, subset,n, k, result):
        lst = ['a', 'b', 'c']
        if len(subset)==n:
            result.append("".join(subset))
            return
        for char in ['a','b','c']:
            if subset and subset[-1]==char:
                continue
            subset.append(char)
            self.solve(subset, n, k, result)
            subset.pop()
            if len(result)==k:
                return

    def getHappyString(self, n: int, k: int) -> str:
        result = []
        self.solve([],n,k,result)
        if len(result) < k:
            return ""

        return result[k-1]            