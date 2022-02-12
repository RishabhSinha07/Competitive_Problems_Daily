class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)-1
        data = {}
        
        def dfs(l,r):
            if (l,r) in data:
                return data[(l,r)]
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l]==s[r]:
                data[(l,r)] = dfs(l+1,r-1)+2
                return data[(l,r)]
            
            data[(l,r)] = max(dfs(l+1,r),dfs(l,r-1))
            return data[(l,r)]
        
        return dfs(0,n)