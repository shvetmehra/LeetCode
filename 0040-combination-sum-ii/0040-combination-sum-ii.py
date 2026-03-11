# BRUTE FORCE
class Solution:
    def solve(self, index, total, subset,candidates, target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if index >= len(candidates):
            return
        for i in range (index, len(candidates)):
            if i>index and candidates[i] == candidates[i-1]:
                continue
            Sum = total + candidates[i]
            subset.append(candidates[i])
            self.solve(i+1, Sum, subset,candidates, target, result)
        
            subset.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.solve(0,0,[], candidates, target, result)
        return result


        