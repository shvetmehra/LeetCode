class StockSpanner:

    def __init__(self):
        self._nums = []
        self._stack = []        

    def next(self, price: int) -> int:
        self._nums.append(price)
        while self._stack and price >= self._nums[self._stack[-1]]:
            self._stack.pop()
        self._stack.append(len(self._nums) - 1)
        return self._stack[-1] - self._stack[-2] if len(self._stack) > 1 else len(self._nums)