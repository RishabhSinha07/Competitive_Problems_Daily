class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        words = sorted(words, key=len)
        for i in words:
            dp[i]=1
            for j in range(len(i)):
                word = i[:j]+i[j+1:]
                if word in dp:
                    dp[i]=1+dp[word]
                    res = max(res, dp[i])
        
        return res