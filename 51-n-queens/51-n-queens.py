class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        
        dp = [[0]*n for _ in range(n)]
        qq = [['.']*n for _ in range(n)]
        
        
        def populate(temp, cx, cy):
            dp = deepcopy(temp)
            for i in range(cx, n):
                dp[i][cy] = 1
            for i in range(0, cx):
                dp[i][cx] = 1
            for i in range(cy, n):
                dp[cx][i] = 1
            for i in range(0, cy):
                dp[cx][i] = 1
            
            nx, ny = cx, cy
            while nx < n and ny < n:
                dp[nx][ny] = 1
                nx+=1
                ny+=1
            
            nx, ny = cx, cy
            while nx >= 0 and ny >=0:
                dp[nx][ny] = 1
                nx-=1
                ny-=1
            
            nx, ny = cx, cy
            while nx < n and ny >= 0:
                dp[nx][ny] = 1
                nx+=1
                ny-=1
            
            nx, ny = cx, cy
            while nx >= 0 and ny < n:
                dp[nx][ny] = 1
                nx-=1
                ny+=1
            
            return dp
        
        def bT(dp, row, qq):
            # for i in qq:
            #     print(i)
            # print('___________')
            if row == n:
                temp = []
                for i in qq:
                    temp.append(''.join(i))
                self.res.append(temp)
                return
            for i in range(len(dp[row])):
                if dp[row][i] == 0:
                    qq[row][i] = 'Q'
                    temp = populate(dp, row, i)
                    bT(temp, row+1, qq)
                    qq[row][i] = '.'
        
        bT(dp, 0, qq)
        return self.res