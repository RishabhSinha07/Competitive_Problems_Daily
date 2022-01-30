class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        z, o = [0]*(N+1), [0]*N
        
        count = 0
        for i in range(N):
            z[i]=count
            if nums[i] == 0:
                count+=1
        z[-1] = count
        
        count = 0
        for i in range(N-1,-1,-1):
            count+=nums[i]
            o[i] = count
        
        for i in range(N):
            z[i]+=o[i]
        
        max_value = max(z)
        return [x for x in range(N+1) if z[x] == max_value]
    
        
        