class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = deque([[0,0,1]])
        ex, ey = len(grid)-1, len(grid)-1 
        
        self.res = float('inf')
        
        while len(q) > 0:
            cx, cy, dt = q.popleft()
            
            if cx == ex and cy == ey:
                self.res = min(self.res, dt)
                continue
            
            for i,j in [[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]]:
                nx = cx+i
                ny = cy+j
                if 0<=nx<=ex and 0<=ny<=ey and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    q.append([nx,ny,dt+1])
                    
        
        if self.res == float('inf'):
            return -1
        return self.res