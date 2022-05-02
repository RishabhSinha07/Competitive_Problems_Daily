class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        
        for i,j in enumerate(nums):
            if j == -1:
                continue
            if j%2 == 0:
                res.append(j)
                nums[i]=-1
        
        for i,j in enumerate(nums):
            if j == -1:
                continue
            if j%2 != 0:
                res.append(j)
                nums[i]=-1
        
        return res