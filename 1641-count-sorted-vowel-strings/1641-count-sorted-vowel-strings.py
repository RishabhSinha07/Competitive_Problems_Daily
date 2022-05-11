class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.res = 0
        
        def help(index,curr):
            if curr == n:
                self.res+=1
                return
            for i in range(index,5):
                help(i,curr+1)

        help(0,0)
        return self.res
