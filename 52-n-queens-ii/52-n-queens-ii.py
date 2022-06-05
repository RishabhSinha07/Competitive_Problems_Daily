class Solution:
    def totalNQueens(self, n: int) -> int:
        MATRIX = [[0]*n for i in range(n)]
        return self.backTracking(MATRIX,0,0,0)
        
    
    def updateMartixWithQueenPos(self,M,x,y):
        edgeX = len(M)
        edgeY = len(M[0])

        VTU = [(x,y)]
        VTU += [(x,z) for z in range(edgeY) if z != y]
        VTU += [(z,y) for z in range(edgeX) if z != x]
        for z1 in range(1,edgeX):
            if x+z1 < edgeX and y+z1 < edgeY:
                VTU.append((x+z1,y+z1))
            if x-z1 > -1 and y-z1 > -1 :
                VTU.append((x-z1,y-z1))
            if x+z1 < edgeX and y-z1 > -1:
                VTU.append((x+z1,y-z1))
            if x-z1 > -1 and y+z1 < edgeY:
                VTU.append((x-z1,y+z1))
        for i in VTU:
            M[i[0]][i[1]] = 1
        return M

    def backTracking(self,M,x,y,count):
        if x == len(M):
            return 1
        for j in range(len(M[x])):
            if M[x][j] == 1 and j == len(M[x])-1:
                return count
            if M[x][j] == 1:
                continue
            else:
                temp = copy.deepcopy(M)
                temp = self.updateMartixWithQueenPos(temp,x,j)
                count+=self.backTracking(temp,x+1,j,0)

        return count