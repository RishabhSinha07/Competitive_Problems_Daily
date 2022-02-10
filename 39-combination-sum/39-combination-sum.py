class Solution:
    def dfs(self, target, index, res):
        if target == 0:
            self.answer.append(res)
        if target < 0:
            return
        for i in range(index, len(self.cand)):
            self.dfs(target-self.cand[i],i,res+[self.cand[i]])
        
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.cand = candidates
        self.dfs(target, 0, [])
        return self.answer