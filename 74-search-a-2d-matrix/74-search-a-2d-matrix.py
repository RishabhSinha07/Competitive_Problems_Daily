class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = []
        for i in matrix:
            if i[0] <= target <= i[-1]:
                targetRow = i
                break
        if target in targetRow: return True
        return False