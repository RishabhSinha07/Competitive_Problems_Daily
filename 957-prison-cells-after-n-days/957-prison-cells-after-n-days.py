class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = (N-1)%14+1
        for _ in range(N):
            temp = [0]*len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    temp[i] = 1
                else:
                    temp[i] = 0
            temp[0] = temp[-1] = 0
            cells = temp
        return cells