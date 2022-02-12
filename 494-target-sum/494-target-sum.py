class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(curr,count):
            if curr == len(nums):
                return 1 if count == target else 0            
            if (curr,count) in cache:
                return cache[(curr,count)]
            
            cache[(curr,count)] = dfs(curr+1,count+nums[curr])+dfs(curr+1,count-nums[curr])
            
            return cache[(curr,count)]
        
        return dfs(0,0)
        