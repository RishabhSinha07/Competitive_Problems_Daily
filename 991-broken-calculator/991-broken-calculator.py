class Solution:
    def brokenCalc(self, sv: int, target: int) -> int:
        res = 0
        
        while sv < target:
            if target%2 == 0:
                target//=2
            else:
                target+=1
            res+=1
        
        res+=(sv-target)
        return res
    