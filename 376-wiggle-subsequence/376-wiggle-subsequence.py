class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [nums[i-1]-nums[i] for i in range(1,len(nums)) if nums[i-1]-nums[i] != 0]
        
        if len(dp) == 0:
            return 1
        
        res = 2
        for i in range(len(dp)-1):
            if dp[i] < 0 and dp[i+1] > 0:
                res+=1
            elif dp[i] > 0 and dp[i+1] < 0:
                res+=1
        return res