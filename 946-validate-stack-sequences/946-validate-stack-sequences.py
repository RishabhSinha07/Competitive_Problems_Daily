class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        queue = collections.deque()
        popIndex = 0
        
        for i in pushed:
            if popIndex >= len(popped):
                return False
            queue.append(i)
            while len(queue) > 0 and popIndex < len(popped):
                if queue[-1] == popped[popIndex]:
                    queue.pop()
                    popIndex+=1
                else:
                    break
                    
        return popIndex >= len(popped) and len(queue) == 0
            