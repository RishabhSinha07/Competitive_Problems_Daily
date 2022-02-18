class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = list()
        
        for i in num:
            while k>0 and result and result[-1]>i:
                result.pop(-1)
                k-=1
            if result or i != '0':
                result.append(i)
        
        if k>0:
            result = result[0:-k]
            
        
        return ''.join(result) or '0'
