class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        left = 0
        right = 0
        blank = 0
        for i in range (n):
            if moves[i]=="L":
                left +=1
            elif moves[i]=='R':
                right +=1
            else:
                blank +=1
        if left >=right:
            return left + blank - right
        else:
            return right + blank - left 
        