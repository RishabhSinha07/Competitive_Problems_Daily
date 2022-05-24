class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # stack, used to record index of parenthesis
        # initialized to -1 as dummy head for valid parentheses length computation
        stack = [-1]
        
        max_length = 0
        
		# linear scan each index and character in input string s
        for cur_idx, char in enumerate(s):
            
            if char == '(':
                
                # push when current char is (
                stack.append( cur_idx )
                
            else:
                
                # pop when current char is )
                stack.pop()
                
                if not stack:
                    
                    # stack is empty, push current index into stack
                    stack.append( cur_idx )
                else:
                    # stack is non-empty, update maximal valid parentheses length
                    max_length = max(max_length, cur_idx - stack[-1])
                
        return max_length