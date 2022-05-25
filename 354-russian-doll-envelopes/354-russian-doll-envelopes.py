class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        # For each value we want to check the left values that can fit inside
        # the current value. To make sure we don't overfit we sort this way
        e.sort(key = lambda x : (x[0],-x[1]))
        
        # Ec
        if len(e) == 1:
            return 1
        if len(e) == 0:
            return 0
        
        # DP
        dp = []
        for w,h in e:
            
            start = bisect_left(dp, h)
            
            if start == len(dp):
                dp.append(h)
            else:
                dp[start] = h
                
        return len(dp)
        
        