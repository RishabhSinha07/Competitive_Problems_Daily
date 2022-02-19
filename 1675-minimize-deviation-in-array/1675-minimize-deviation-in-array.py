class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        
        for i in nums:
            v1 = v2 = i
            while v1%2 == 0:
                v1 = v1//2
            
            if v2%2 != 0:
                v2*=2
            
            heappush(h,(v1,v2))
        
        self.res = float('inf')
        mx = max([x for x,y in h])
        
        while len(h) == len(nums):
            curr,limit = heappop(h)
            self.res = min(self.res, mx-curr)
            if curr < limit:
                heappush(h,(curr*2,limit))
                mx = max(mx,curr*2)
        
        return self.res
        