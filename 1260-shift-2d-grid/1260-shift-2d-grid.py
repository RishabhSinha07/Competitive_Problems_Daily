class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            temp = grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid[i][j], temp = temp, grid[i][j]
            grid[0][0] = temp
        
        return grid