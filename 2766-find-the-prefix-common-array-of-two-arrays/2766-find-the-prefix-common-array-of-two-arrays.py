class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        m = len(A)
        n = len(B)
        ans = set()
        res = []
        count = 0
        for i in range (n):
            if A[i] in ans:
                count +=1
            else:
                ans.add (A[i])
            if B[i] in ans:
                count +=1
            else:
                ans.add(B[i])
            res.append(count)
        return res

        