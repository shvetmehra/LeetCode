class Solution:
    def solve(self, col, board, ans, leftrow, updiag, lowdiag, n):
        if col == n:
            ans.append(board[:])
            return
        for row in range(n):
            if (
                leftrow[row] == 0
                and updiag[n-1+col-row]==0
                and lowdiag[row+col]==0
            ):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                leftrow[row]=1
                updiag[n-1+col-row]=1
                lowdiag[col+row]=1

                self.solve(col+1,board,ans, leftrow,updiag,lowdiag,n)
                board[row]=board[row][:col]+'.'+board[row][col+1:]
                leftrow[row]=0
                updiag[n-1+col-row]=0
                lowdiag[col+row]=0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.' *n for _ in range(n)]
        leftrow = [0]*n
        updiag = [0]*(2*n-1)
        lowdiag = [0]*(2*n-1)
        self.solve(0, board, ans, leftrow, updiag, lowdiag, n )
        return ans