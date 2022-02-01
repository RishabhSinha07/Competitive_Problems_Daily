class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        NGE = [x for x in prices]
        
        result = 0
        for i in range(len(prices)-2,-1,-1):
            NGE[i] = max(prices[i],NGE[i+1])
            result = max(result, NGE[i]-prices[i])
        
        return result
            
        