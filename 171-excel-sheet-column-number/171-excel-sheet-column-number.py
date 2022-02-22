class Solution:
    def titleToNumber(self, cT: str) -> int:
        cT = cT.lower()
        result, bit, size = 0, 26, len(cT)-1
        
        for i,j in enumerate(cT):
            result = result + (bit**(size-i))*(ord(j)-ord('a')+1)
        
        return result