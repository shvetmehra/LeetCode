from copy import deepcopy
from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #BFS
        if image[sr][sc]==color:
            return image
        visited = deepcopy(image)
        rows,cols = len(visited),len(visited[0])
        initial_color = visited[sr][sc]
        queue = deque()
        queue.append((sr,sc))

        while len(queue)!=0:
            i,j = queue.popleft()
            visited[i][j]=color
            for x,y in [(0,1), (1,0), (-1,0), (0,-1)]:
                newi = i+x
                newj = j+y
                if newi <0 or newi>=rows or newj<0 or newj>=cols:
                    continue
                if visited[newi][newj]!=initial_color:
                    continue
                queue.append((newi,newj))
        return visited  

