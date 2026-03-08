class Solution:
    def solve (self, index, total, parenthesis, result):
        if index >= len(parenthesis):
            if total ==0:
                result.append(''.join(parenthesis))
            return
        if total >= len(parenthesis):
            return
        elif total < 0:
            return 
        parenthesis[index]='('
        self.solve(index+1, total+1, parenthesis, result)
        
        parenthesis[index]=')'
        
        self.solve(index+1, total-1, parenthesis, result)
        parenthesis[index]='('
    
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = ['']*2*n
        result = []
        self.solve(0, 0, parenthesis, result)
        return result        