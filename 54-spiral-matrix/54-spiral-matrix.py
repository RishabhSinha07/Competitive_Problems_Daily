class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        '''
        Basically we want to follow a certain path which is from current 
        position go 'right' then 'down' then 'left' and then 'up'. Keep
        the sequence untill we have visited all the values. 
        [(0,1),(-1,0),(0,-1),(1,0)]
        
        The main thing here is to understnad when to switch. It is possible only when:
        1. when we reach the boundary
        2. when we encounter already visited element
        
        TC : O(n**2)
        '''
        
        R, C = len(matrix), len(matrix[0])

        path, visited, result = [(0,1),(1,0),(0,-1),(-1,0)], [], []
        x, y, i = 0, 0, 0
        
        for _ in range(R*C):
            print(x,y)
            result.append(matrix[x][y])
            
            nx, ny, count = x+path[i][0], y+path[i][1], 0
            while  nx < 0 or nx >= R or ny < 0 or ny >= C or (nx,ny) in visited:
                if count > 5:
                    break
                i = (i+1)%4
                nx, ny = x+path[i][0], y+path[i][1]
                count+=1
                
            visited.append((x,y))    
            x, y = nx, ny
            
                
        return result
        