class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Move from destination to starting point. 
        For each point calculate the min jumps required. 
        Min jump can be found by getting the lowest just for the
        next nums[i] elements from ith position and adding +1 to it
        to execute the jump. 
        
        For index with value 0 assign the max threshold value as it is not
        possible to jump from there and there is always a unique solution. 
        Therefore it won't be an issue. 
        
        TC : O(N*K) where K is avg size of nums[i] and N is len of arr
        SC : O(N) for dp
        
        '''
        
        N = len(nums)
        dp = [0]*N
        
        for i in range(N-2,-1,-1):
            if  nums[i] == 0: 
                dp[i] = 1001
                continue
            dp[i] = min(dp[i+1:i+nums[i]+1])+1
        
        return dp[0]
    