n = 1000001
prime_divisors = [[] for _ in range(n)]
for k in range(2, n//2+1):
    if not prime_divisors[k]:
        for i in range(k, n, k):
            prime_divisors[i].append(k)
        
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        dic_nums = defaultdict(list)
        for i, num in enumerate(nums):
            dic_nums[num].append(i)

        n = len(nums)
        que, dist = deque([n-1]), [-1] * (n+1)
        dist[-2:] = (0, 0)
        while i := que.pop():
            for prime in prime_divisors[nums[i]]:
                for j in dic_nums[prime]:
                    if dist[j] < 0:
                        que.appendleft(j)
                        dist[j] = dist[i] + 1
            if dist[i-1] < 0:
                que.appendleft(i-1)
                dist[i-1] = dist[i] + 1
            if dist[i+1] < 0:
                que.appendleft(i+1)
                dist[i+1] = dist[i] + 1
        return dist[0]