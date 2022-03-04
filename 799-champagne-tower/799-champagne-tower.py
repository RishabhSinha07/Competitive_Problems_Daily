class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        levels = [[0]*i for i in range(1,query_row+2)]
        levels[0] = [poured]
        
        for i in range(len(levels)-1):
            for j in range(len(levels[i])):
                if levels[i][j]-1 <= 0: continue
                temp = (levels[i][j]-1)/2.0
                levels[i+1][j] = levels[i+1][j]+temp
                levels[i+1][j+1] = levels[i+1][j+1]+temp
                

        
        return min(1,levels[query_row][query_glass])