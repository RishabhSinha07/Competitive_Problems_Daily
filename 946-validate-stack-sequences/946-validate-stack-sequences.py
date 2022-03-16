class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Create variables to store pushed and popped information
        queue = collections.deque()
        popIndex = 0
        
        for i in pushed:
            # If there is no value to pop then we cannot complete the process
            if popIndex >= len(popped):
                return False
            queue.append(i)
            # Try to pop as much value as possible
            while len(queue) > 0 and popIndex < len(popped):
                if queue[-1] == popped[popIndex]:
                    queue.pop()
                    popIndex+=1
                else:
                    break
                    
        return popIndex >= len(popped) and len(queue) == 0
        
        """
        TC : O(N+M) where N = len(pushed) and M = len(popped)
        SC : O(N)
        
        Runtime: 87 ms, faster than 69.83% of Python3 online submissions for Validate Stack Sequences.
        Memory Usage: 14.1 MB, less than 93.97% of Python3 online submissions for Validate Stack Sequences.
        """