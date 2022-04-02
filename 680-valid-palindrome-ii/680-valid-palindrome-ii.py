class Solution:
    def check(self, l, r, s):
        while l < r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        
        while l<=r:
            if s[l]!=s[r]:
                return self.check(l+1,r,s) or self.check(l,r-1,s)
            l+=1
            r-=1
        
        return True