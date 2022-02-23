class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pv, nv = [], []
        
        for i in nums:
            if i > 0:
                pv.append(i**2)
            else:
                nv.append(i**2)
        
        result = []
        pi,ni=0,len(nv)-1
        while pi<len(pv) and ni>-1:
            if pv[pi] <= nv[ni]:
                result.append(pv[pi])
                pi+=1
            else:
                result.append(nv[ni])
                ni-=1
        
        if pi < len(pv):
            result+=pv[pi:]
        if ni > -1:
            result+=nv[:ni+1][::-1]
        
        return result
        