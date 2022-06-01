class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ps = 0
        
        for i in range(len(nums)):
            ps+=nums[i]
            nums[i]=ps
        
        return nums