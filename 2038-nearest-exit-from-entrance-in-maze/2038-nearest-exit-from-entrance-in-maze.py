from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        visited = [[False for _ in range (cols)] for _ in range (rows)]
        
        start_r, start_c = entrance
        queue = deque([(start_r, start_c, 0)])
        visited[start_r][start_c]=True

        while len(queue)!=0:
            r,c,d = queue.popleft()
            
            for x, y in [(-1,0), (0,-1), (1,0), (0,1)]:
                nr, nc = r+x, c+y
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                if not visited [nr][nc] and maze[nr][nc]=='.':
                    if nr==0 or nr==rows-1 or nc==0 or nc==cols-1:
                        return d+1
                        
                    visited[nr][nc]=True
                    queue.append((nr, nc, d+1))
        return -1