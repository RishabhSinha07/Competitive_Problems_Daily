class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row, self.col = len(matrix), len(matrix[0])
        self.matrix = matrix
        
        for i in range(self.row):
            for j in range(1,self.col):
                self.matrix[i][j]+=self.matrix[i][j-1]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        while row1 <= row2:
            cx, cy = row1, col1
            nx, ny = row1, col1 + (col2-col1)
            
            res+=self.matrix[nx][ny]
            if 0<=cy-1:
                res-=self.matrix[cx][cy-1]
            row1+=1
        return res
        
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)