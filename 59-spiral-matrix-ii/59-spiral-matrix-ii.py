class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.path = [[0,1],[1,0],[0,-1],[-1,0]]
        self.visited = collections.defaultdict(bool)
        self.res = [[0]*n for _ in range(n)]
        self.pos = 0
        
        def insert(x,y,value):
            if self.visited[(x,y)] or x >= n or y >= n or x < 0 or y < 0:
                return
            self.visited[(x,y)] = 1
            self.res[x][y] = value
            
            nx = x + self.path[self.pos][0]
            ny = y + self.path[self.pos][1]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or self.visited[(nx,ny)]:
                self.pos+=1
                self.pos%=4
            
            x = x + self.path[self.pos][0]
            y = y + self.path[self.pos][1]
            insert(x,y,value+1)
        
        insert(0,0,1)
        return self.res