class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        result_st = ""
        for i in range(len(s)):
            result = max(result, self.expand(i,i,s))
            result = max(result, self.expand(i,i+1,s))
            
            if result > len(result_st):
                start = i-(result-1)//2
                end = i+result//2
                result_st = s[start:end+1]
                
        
        return result_st
    
    def expand(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right-left-1