class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        We need to go through each element twice. And check for number of plaindromes.  
        For abc
        
        aa
        ab
        bb
        bc
        cc
        
        pointer1 : a,a,b,b,c,....
        pointer2 : a,b,b,c,c,....
        
        Total number of points : 2*len(s)-1
        '''
        
        N = len(s)
        
        res = 0
        for i in range(2*N-1):
            p1 = i//2
            p2 = i//2+i%2
            
            while p1 >= 0 and p2 < N and s[p1] == s[p2]:
                res+=1
                p1-=1
                p2+=1
        
        return res