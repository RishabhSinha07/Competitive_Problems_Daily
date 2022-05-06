class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
            if len(stack)>0 and stack[-1][1] == k:
                stack.pop()
            
            if len(stack) == 0 or stack[-1][0] != i:
                stack.append([i,1])
            else:
                stack[-1][1]+=1
        
        if len(stack)>0 and stack[-1][1] == k:
            stack.pop()
        
        res = ""
        for i in stack:
            res+=i[0]*i[1]
        
        return res