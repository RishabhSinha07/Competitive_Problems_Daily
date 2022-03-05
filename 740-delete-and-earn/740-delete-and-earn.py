from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        l = sorted(list(d.keys()))
        if len(l) == 1:
            return l[0] * d[l[0]]
        
        i = 2
        prev1 = (l[0] * d[l[0]], l[0])
        if l[0] != l[1] - 1:
            prev2 = (prev1[0] + l[1] * d[l[1]], l[1])
        else:
            prev2 = (max(l[1] * d[l[1]], prev1[0]), l[1])
            
            
        while i < len(l):
            if l[i] != prev2[1] + 1:
                aux = (prev2[0] + l[i] * d[l[i]], l[i])
            else:
                aux = (max(prev1[0] + l[i] * d[l[i]], prev2[0]) ,l[i])
            prev1 = prev2
            prev2 = aux
            i += 1
        return prev2[0]