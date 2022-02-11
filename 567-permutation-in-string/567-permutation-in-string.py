class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tracker = [0]*26
        
        for i in s1:
            tracker[ord(i)-ord('a')]+=1
        
        temp = [0]*26
        slow, fast = 0, 0
        
        while fast < len(s2):
            temp[ord(s2[fast]) - ord('a')]+=1
            if temp == tracker:
                return True
            if fast-slow+1 > len(s1):
                temp[ord(s2[slow]) - ord('a')]-=1
                slow+=1
            fast+=1
            
            if temp == tracker:
                return True
        
        return False
                