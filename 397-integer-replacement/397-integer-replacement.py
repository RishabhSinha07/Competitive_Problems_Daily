class Solution:
    def approach1(self,n):
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
    
    
    def integerReplacement(self, n: int) -> int:
        self.result = 0
        
        while n > 1:
            print(n)
            if n%2 == 0:
                n=n//2
                self.result+=1
            else:
                temp = (n-1)//2
                if temp % 2 == 0 or temp == 1:
                    n = n-1
                else:
                    n = n+1
                self.result+=1
            
        
        return self.result