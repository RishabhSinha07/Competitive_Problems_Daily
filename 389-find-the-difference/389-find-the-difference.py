class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp = collections.defaultdict(int)
        
        for i in s:
            temp[i]+=1
            
        for i in t:
            if temp[i] == 0:
                return i
            else:
                temp[i]-=1
        
        return ""