class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        
        for i in t:
            if index >= len(s):
                return True
            if s[index] == i:
                index+=1
                
        if index >= len(s): return True
        return False