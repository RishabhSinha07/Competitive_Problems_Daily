class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
            if len(stack)>0 and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
            
            if len(stack) == 0 or stack[-1][0] != i:
                stack.append([i,1])
            else:
                stack.append([i,stack[-1][1]+1])
        
        if len(stack)>0 and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        
        return ''.join(x[0] for x in stack)    
        