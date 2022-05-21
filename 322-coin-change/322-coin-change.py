class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        
        dp[0] = 0
        
        for i in range(1,len(dp)):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], 1+dp[i-j])
        
        if dp[-1] > amount:
            return -1
        return dp[-1]