class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, res = 0, ""
        
        for i in range(len(s)):
            if s[i] not in res:
                res+=s[i]
            else:
                index = res.index(s[i])
                res = res[index+1:]+s[i]
            ans = max(ans, len(res))
        
        return ans