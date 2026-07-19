class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visited = [0]*26
        nums = [0]*26
        for ch in s:
            nums[ord(ch)-ord('a')]+=1
        res = []
        for ch in s:
            index = ord(ch) - ord('a')
            if not visited[index]:
                while res and res[-1]>ch:
                    new_index = ord(res[-1]) - ord('a')
                    if nums[new_index]>0:
                        visited[new_index]=0
                        res.pop()
                    else:
                        break
                visited[index]=1
                res.append(ch)
            nums[index]-=1
        return "".join(res)
        