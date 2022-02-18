class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = list()
        
        
        for i in num:
            while res and res[-1]>i and k > 0:
                res.pop()
                k-=1
            res.append(i)
        
        while k:
            res.pop()
            k-=1
        
        return "".join(res).lstrip('0') or "0"