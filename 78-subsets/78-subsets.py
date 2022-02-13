class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.visited = {}
        
        def dfs(nums, curr):
            if tuple(curr) in self.visited:
                return
            self.res.append(curr)
            self.visited[tuple(curr)] = True
            for i in range(len(nums)):
                dfs(nums[i+1:],curr+[nums[i]])
                dfs(nums[i+1:],curr)
        
        dfs(nums,[])
        return self.res
                
                
            