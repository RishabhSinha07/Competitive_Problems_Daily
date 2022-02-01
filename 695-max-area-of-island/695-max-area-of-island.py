class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        space  O(n * m)
        time   O(n * m * a(n * m))
        
        '''
        m, n = len(grid), len(grid[0])
        parent = [-1] * (m * n)
        
        def find(x):
            i = x
            while parent[i] >= 0:
                i = parent[i]
                parent[x] = i         
            return i
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return 
            if px > py:
                px, py = py, px 
            parent[px] += parent[py]
            parent[py] = px
        
        offsets = [[0,1],[1,0],[-1,0],[0,-1]]
        foundIsland = False
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    foundIsland = True
                    for offsetrow, offsetcol in offsets:
                        r = row + offsetrow
                        c = col + offsetcol
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                            union(row * n + col, r * n + c)
        if not foundIsland:
            return 0
        return -min(parent)