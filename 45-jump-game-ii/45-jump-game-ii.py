class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        
        for i in range(N-2,-1,-1):
            if  nums[i] == 0: 
                dp[i] = 1001
                continue
            dp[i] = min(dp[i+1:i+nums[i]+1])+1
        
        return dp[0]
    