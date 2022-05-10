"""

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

k = 3 and N = 7
-> 1,2,4

"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        
        def help(k, curr, temp, n):
            if k == 0:
                if sum(temp) == n:
                    self.res.append(temp)
                return
            if k > 0 and sum(temp) > n:
                return
            for i in range(curr, 10):
                help(k-1, i+1, temp+[i], n)
        
        help(k,1,[],n)

        return self.res

