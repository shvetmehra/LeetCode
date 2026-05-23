class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(char) for char in s.split() if char.isdigit()]
        for i in range (len(numbers)-1):
            if numbers[i]>=numbers[i+1]:
                return False
        return True