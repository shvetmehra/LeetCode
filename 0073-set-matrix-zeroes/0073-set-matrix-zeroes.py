class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix [0])
        rowTrack = [0 for _ in range(r)]
        colTrack = [0 for _ in range(c)]

        for i in range (0,r):
            for j in range (0,c):
                if matrix[i][j]==0:
                    rowTrack[i]=-1
                    colTrack[j]=-1
            
        for i in range (0,r):
            for j in range(0,c):
                if rowTrack[i]==-1 or colTrack[j]==-1:
                    matrix[i][j]=0