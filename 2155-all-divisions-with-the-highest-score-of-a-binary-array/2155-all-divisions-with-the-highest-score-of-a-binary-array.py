class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        zeroes = [0]*(N+1)
        
        count = 0
        for i in range(N):
            zeroes[i]=count
            if nums[i] == 0:count+=1
        zeroes[-1] = count
        
        count = 0
        for i in range(N-1,-1,-1):
            count+=nums[i]
            zeroes[i] += count
        
        max_value = max(zeroes)
        return [x for x in range(N+1) if zeroes[x] == max_value]
    
        
        