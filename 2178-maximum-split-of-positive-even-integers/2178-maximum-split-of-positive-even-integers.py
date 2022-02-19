class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        x = finalSum//2
        
        res = []
        if finalSum%2 == 0:
            ns = 2
            while ns <= finalSum:
                res.append(ns)
                finalSum-=ns
                ns+=2
                
        
            res[-1]+=finalSum
        
        return res
