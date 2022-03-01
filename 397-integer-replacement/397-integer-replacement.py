class Solution:
    def integerReplacement(self, n: int) -> int:
        self.result = 10**10
        
        def rec(curr, count):
            if curr == 1:
                self.result = min(self.result, count)
                return
            
            if curr%2 == 0:
                rec(curr//2, count+1)
            else:
                rec(curr-1, count+1)
                rec(curr+1, count+1)
        
        rec(n,0)
        return self.result