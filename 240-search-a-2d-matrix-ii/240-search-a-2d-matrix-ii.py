# TC : mlog(n)
# SC : O(1)

class Solution:
    def binarySearch(self, row, l, r, target):
        while l < r:
            mid = l+(r-l)//2
            if row[mid] >= target:
                r = mid
            else:
                l = mid+1
        return row[l] == target
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1] and self.binarySearch(row,0,len(row)-1,target):
                return True
        return False