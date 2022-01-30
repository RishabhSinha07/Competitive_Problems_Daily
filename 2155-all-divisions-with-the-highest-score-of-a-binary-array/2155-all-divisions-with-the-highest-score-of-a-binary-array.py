class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        values = [0]*(N+1)
        
        count = 0
        for i in range(N):
            values[i]=count
            if nums[i] == 0:count+=1
        values[-1] = count
        
        count = 0
        for i in range(N-1,-1,-1):
            count+=nums[i]
            values[i] += count
        
        max_value = max(values)
        return [x for x in range(N+1) if values[x] == max_value]
    
        
        