class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ps = 0
        
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        
        return nums