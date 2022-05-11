# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         self.res = 0
#         self.dp = {}
        
#         def help(index,curr):
#             if (index,curr) in self.dp:
#                 return self.dp[(index,crr)]
#             if curr == n:
#                 self.res+=1
#                 return 0
#             for i in range(index,5):
#                 self.dp[(i,crr+1)] = help(i,curr+1)

#         help(0,0)
#         return self.res

class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
		#initialised the table with 1
        dp = [[1]*5 for i in range(n+1)]
		
        for i in range(1,n+1):
            for j in range(3,-1,-1):
                dp[i][j] = dp[i][j+1]+dp[i-1][j]
                
        return dp[n][0]
