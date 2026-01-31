class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows,cols = len(image), len(image[0])
        initial_color = image[sr][sc]

        if initial_color == color:
            return image

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols:
                return
            if image[i][j] == color:
                return
            if image[i][j] != initial_color:
                return
        
            image[i][j]=color
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        dfs(sr,sc)
        return image
    