class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.res = 0
        self.vow = ['a','e','i','o','u']
        
        def help(index,curr):
            if len(curr) == n:
                self.res+=1
                return
            for i in range(index,len(self.vow)):
                help(i,curr+self.vow[i])

        help(0,"")
        return self.res
