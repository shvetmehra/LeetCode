class Solution:
    def fib(self, n: int) -> int:
        arr = [0,1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range (2, n+1):
                next = arr[i-2]+arr[i-1]
                arr.append(next)
        return arr[-1]
        